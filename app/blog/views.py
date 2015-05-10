from flask import Blueprint
from flask import render_template
from app.models import Post

blog = Blueprint('blog', __name__, url_prefix='/blog')


@blog.route('/')
def home():
    posts = Post.query.all()
    return render_template('blog/home.html', posts=posts)


@blog.route('/<int:post_id>')
def post(post_id):
    return "This is the blog post {}".format(post_id)
