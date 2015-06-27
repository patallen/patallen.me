from app import db
from app.models import Post, Category
from flask import abort, Blueprint, redirect, render_template, url_for, request
from flask_login import login_required, current_user
from .forms import PostForm, DeleteForm
from app.util.errors import NoPostsFound, InvalidCategory, PostNotFound, Unauthorized


blog = Blueprint('blog', __name__, url_prefix='/blog')

POSTS_PER_PAGE = 5


@blog.context_processor
def category_processor():
    """Makes categories available to templates"""
    return dict(categories=Category.query.all())


@blog.route('/')
@blog.route('/category/<category_slug>/')
def home(category_slug=None):
    """Blog home function - takes page number"""
    # If no such category, raise exception
    if category_slug:
        try:
            category = Category.query.filter_by(slug=category_slug).one()
        except:
            raise InvalidCategory("The specified category does not exist.")
    
    page = request.args.get('page', 1)
    query = Post.query
    if category_slug:
        query = Post.query.filter_by(category=category)

    pagination = query.order_by(Post.date_created.desc()).paginate(int(page), POSTS_PER_PAGE, False)

    return render_template('blog/home.html',
                           category_slug=category_slug,
                           pagination=pagination)


@blog.route('/post/<post_slug>/')
def post(post_slug):
    """Return a post by its slug"""
    try:
        post = Post.query.filter_by(slug=post_slug).one()
    except:
        raise PostNotFound("The post you are looking for could not be found.")
    return render_template('blog/post.html', post=post,
                           category_slug=post.category.slug)


@blog.route('/post/add/', methods=['GET', 'POST'])
@login_required
def addPost():
    """Return add post form or process new blog post"""
    form = PostForm()
    form.category.choices = [(c.id, c.name) for c in Category.query.all()]
    form.category.choices.insert(0, (0, 'Select...'))

    if form.validate_on_submit():
        author = current_user.id
        title = form.title.data
        body_md = form.body.data
        category = form.category.data
        post = Post(author, category, title, body_md)
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('blog.post', post_slug=post.slug))

    return render_template('blog/compose.html', form=form)


@blog.route('/post/<post_slug>/edit/', methods=['GET', 'POST'])
@login_required
def editPost(post_slug):
    """Edit an existing blog post"""
    post = Post.query.filter_by(slug=post_slug).one()
    # Check that user is the owner of the project (not necessary atm)
    if current_user.id != post.author:
        raise Unauthorized("You don't have permission to edit this post.") 
    form = PostForm()
    form.category.choices = [(c.id, c.name) for c in Category.query.all()]
    if form.validate_on_submit():
        post.title = form.title.data
        post.body_md = form.body.data
        post.category_id = form.category.data
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('blog.post', post_slug=post.slug))

    # Pre-populate form with existing data
    form.title.data = post.title
    form.body.data = post.body_md
    form.category.data = post.category_id

    return render_template('blog/compose.html', form=form, post=post)

@blog.route('/post/<post_slug>/delete/', methods=['GET', 'POST'])
@login_required
def deletePost(post_slug):
    """Route to delete an existing blog post"""
    post = Post.query.filter_by(slug=post_slug).one()
    if current_user.id != post.author:
        raise Unauthorized("You don't have permission to delete this post.") 
    form = DeleteForm()
    if form.validate_on_submit():
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('blog.home'))
    return render_template('blog/delete.html', form=form, post=post)
