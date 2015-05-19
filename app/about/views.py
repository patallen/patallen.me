from flask import Blueprint, render_template, redirect, url_for
from app.models import Post

about = Blueprint('about', __name__, url_prefix='/')

@about.route('/')
def home():
	"""Home page view - compilation of about info
	and featured posts"""
        recent_posts = Post.query.order_by(Post.date_created.desc()).limit(4)
	return render_template('about/home.html', recent_posts=recent_posts)
