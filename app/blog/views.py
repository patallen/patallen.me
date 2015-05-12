from flask import Blueprint
from flask import abort
from flask import redirect 
from flask import url_for 
from flask import render_template
from app.models import Post
from app.helpers import Pagination
from app import db
from .forms import PostForm
from flask_login import login_required

blog = Blueprint('blog', __name__, url_prefix='/blog')

POSTS_PER_PAGE = 5


def getPostsForPage(page, posts_per_page):
    return Post.query.order_by(Post.date_created.desc())\
                     .offset(posts_per_page * page - posts_per_page)\
                     .limit(posts_per_page)

def getNumPosts():
    return Post.query.count()


@blog.route('/', defaults={'page': 1})
@blog.route('/page/<int:page>/')
def home(page=1):
    """Blog home function - takes page number"""
    count = getNumPosts()
    posts = getPostsForPage(page, POSTS_PER_PAGE)
    pagination = Pagination(page, count, POSTS_PER_PAGE)
    return render_template('blog/home.html', posts=posts, pagination=pagination)


@blog.route('/post/<int:post_id>')
def post(post_id):
    """Return a post by its ID"""
    try:
        post = Post.query.get(post_id)
    except:
        abort(404)
    return render_template('blog/post.html', post=post)


@blog.route('/post/add/', methods=['GET', 'POST'])
@login_required
def addPost():
    """Return add post form or process new blog post"""
    form = PostForm()
    
    if form.validate_on_submit():
        post = Post()
        post.author = 1
        post.title = form.title.data
        post.body_md = form.body.data
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('blog.post', post_id=post.id))

    return render_template('blog/add.html', form=form)


@blog.route('/post/<int:post_id>/edit/', methods=['GET', 'POST'])
@login_required
def editPost(post_id):
    """Edit an existing blog post"""
    post = Post.query.get(post_id)
    form = PostForm()
    form.title.data = post.title
    form.body.data = post.body_md

    if form.validate_on_submit():
        post.title = form.title.data
        post.body_md = form.body.data
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('blog.post', post_id=post.id))

    return render_template('blog/edit.html', form=form, post=post)