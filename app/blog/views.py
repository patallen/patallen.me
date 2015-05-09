from flask import Blueprint

blog = Blueprint('blog', __name__, url_prefix='/blog')


@blog.route('/')
def bloghome():
    return "This is the main blog page"


@blog.route('/<int:post_id>')
def blogpost(post_id):
    return "This is the blog post {}".format(post_id)
