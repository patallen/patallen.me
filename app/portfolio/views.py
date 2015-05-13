from flask import Blueprint
from flask import render_template
from app.models import Project

portfolio = Blueprint('portfolio', __name__, url_prefix='/portfolio')


@portfolio.route('/')
def home():
	"""Main portfolio page - displays list of projects"""
	projects = Project.query.all()
	return render_template('portfolio/home.html', projects=projects)


@portfolio.route('/<int:project_id>')
def project(project_id):
	"""Returns a single project by its ID"""
	return "This is the work piece {}".format(project_id)
