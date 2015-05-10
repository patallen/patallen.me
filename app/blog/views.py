from flask import Blueprint
from flask import abort
from flask import render_template
from app.models import Post
from app.helpers import Pagination

blog = Blueprint('blog', __name__, url_prefix='/blog')

POSTS_PER_PAGE = 5


def getPostsForPage(page, posts_per_page):
    return Post.query.offset(posts_per_page * page - posts_per_page)\
            .limit(posts_per_page)


def getNumPosts():
    return Post.query.count()


@blog.route('/', defaults={'page': 1})
@blog.route('/page/<int:page>/')
def home(page=1):
    count = getNumPosts()
    posts = getPostsForPage(page, POSTS_PER_PAGE)
    pagination = Pagination(page, 11, POSTS_PER_PAGE)
    return render_template('blog/home.html', posts=posts, pagination=pagination)


@blog.route('/post/<int:post_id>')
def post(post_id):
    try:
        post = Post.query.get(post_id)
    except:
        abort(404)
    return render_template('blog/post.html', post=post)
