from flask import Blueprint
from flask import render_template 

portfolio = Blueprint('portfolio', __name__, url_prefix='/portfolio')


@portfolio.route('/')
def home():
	"""Main portfolio page - displays list of projects"""
    return render_template('portfolio/home.html')


@portfolio.route('/<int:project_id>')
def project(project_id):
	"""Returns a single project by its ID"""
    return "This is the work piece {}".format(project_id)
