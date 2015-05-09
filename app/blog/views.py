from flask import Blueprint
from flask import render_template

blog = Blueprint('blog', __name__, url_prefix='/blog')


@blog.route('/')
def home():
    return render_template('blog/home.html')


@blog.route('/<int:post_id>')
def post(post_id):
    return "This is the blog post {}".format(post_id)
