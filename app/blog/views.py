from flask import Blueprint, redirect, render_template, url_for, request
from flask_login import login_required, current_user

from app import db
from app.blog.forms import PostForm, DeleteForm
from app.models import Post, Category
from app.util.errors import Unauthorized, ResourceNotFound
from app.util.functions import get_or_404, get_posts_query


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

    page = request.args.get('page', 1)
    category = Category.query.filter_by(slug=category_slug).first()
    query = get_posts_query(category)
    pagination = (query.order_by(Post.date_created.desc())
                       .paginate(int(page), POSTS_PER_PAGE, False))

    return render_template('blog/home.html',
                           category_slug=category_slug,
                           pagination=pagination)


@blog.route('/post/<post_slug>/')
def post(post_slug):
    """Return a post by its slug"""
    post = get_or_404(Post, slug=post_slug)

    # TODO: I feel this should be done in a
    # Post-specific function
    if post.author != current_user:
        if not post.published:
            raise ResourceNotFound('Post cannot be found.')

    return render_template('blog/post.html', post=post,
                           category_slug=post.category.slug)


@blog.route('/post/add/', methods=['GET', 'POST'])
@login_required
def addPost():
    """Return add post form or process new blog post"""
    form = PostForm()

    if form.validate_on_submit():
        post = Post(title=form.title.data)
        form.populate_obj(post)
        post.author = current_user
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('blog.post', post_slug=post.slug))

    return render_template('blog/compose.html', form=form)


@blog.route('/post/<post_slug>/edit/', methods=['GET', 'POST'])
@login_required
def editPost(post_slug):
    """Edit an existing blog post"""
    post = get_or_404(Post, slug=post_slug)

    if current_user != post.author:
        raise Unauthorized("You don't have permission to edit this post.")

    form = PostForm(obj=post)

    if form.validate_on_submit():
        form.populate_obj(post)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('blog.post', post_slug=post.slug))

    return render_template('blog/compose.html', form=form, post=post)


@blog.route('/post/<post_slug>/delete/', methods=['GET', 'POST'])
@login_required
def deletePost(post_slug):
    """Route to delete an existing blog post"""
    post = get_or_404(Post, slug=post_slug)

    if current_user != post.author:
        raise Unauthorized("You don't have permission to delete this post.")

    form = DeleteForm()
    if form.validate_on_submit():
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('blog.home'))
    return render_template('blog/delete.html', form=form, post=post)
