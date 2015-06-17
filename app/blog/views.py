from app import db
from app.helpers import Pagination
from app.models import Post, Category
from flask import abort, Blueprint, redirect, render_template, url_for, request
from flask_login import login_required, current_user
from .forms import PostForm
from app.util.errors import NoPostsFound


blog = Blueprint('blog', __name__, url_prefix='/blog')

POSTS_PER_PAGE = 5.0


def filterPostsByCategory(category_slug):
    """Returns a Post query set filtered by category_slug"""
    return Post.query.filter(Post.category.has(Category.slug == category_slug))


def getPostsForPage(page, posts_per_page, category_slug=''):
    """Gets posts for home blog page -- category_slug is optional"""
    postQuery = Post.query
    # Filter by category_slug if it exists
    if category_slug:
        postQuery = filterPostsByCategory(category_slug)
    # Return resulting query offset & limited for given page
    posts = postQuery.order_by(Post.date_created.desc())\
                    .offset(posts_per_page * page - posts_per_page)\
                    .limit(posts_per_page)
    if len(posts.all()) < 1:
        raise NoPostsFound("No posts were found for this category.")
    return posts 


def getNumPosts(category_slug=None):
    """Gets total number of posts or total number of posts
    within a specific category if category_slug provided"""
    if category_slug:
        return filterPostsByCategory(category_slug).count()
    return Post.query.count()


@blog.context_processor
def category_processor():
    """Makes categories available to templates"""
    return dict(categories=Category.query.all())


@blog.route('/')
@blog.route('/category/<category_slug>/')
def home(category_slug=None):
    """Blog home function - takes page number"""
    page = 1
    if request.args.get('page'):
        page = int(request.args.get('page'))
    count = getNumPosts(category_slug)
    posts = getPostsForPage(page, POSTS_PER_PAGE, category_slug=category_slug)
    pagination = Pagination(page, count, POSTS_PER_PAGE)

    if not posts:
       return "No posts for this category." 
    return render_template('blog/home.html', posts=posts,
                           pagination=pagination, category_slug=category_slug)


@blog.route('/post/<post_slug>/')
def post(post_slug):
    """Return a post by its slug"""
    try:
        post = Post.query.filter_by(slug=post_slug).one()
    except:
        abort(404)
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
        return "You do not have permission to edit this blog post."
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
