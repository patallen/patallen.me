from flask import Blueprint, render_template, redirect, url_for
from app.models import Post
from app.util.functions import get_posts_query

about = Blueprint('about', __name__, url_prefix='/')

@about.route('/')
def home():
    """Home page view - compilation of about info
    and featured posts"""
    query = get_posts_query(published_only=True)
    recent_posts = query.order_by(Post.date_created.desc()).limit(4)
    return render_template('about/home.html', recent_posts=recent_posts)
