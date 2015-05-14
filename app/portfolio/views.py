from flask import Blueprint
from flask import render_template
from app.models import Project
from .forms import ProjectForm
from flask_login import login_required

portfolio = Blueprint('portfolio', __name__, url_prefix='/portfolio')


@portfolio.route('/')
def home():
	"""Main portfolio page - displays list of projects"""
	projects = Project.query.all()
	return render_template('portfolio/home.html', projects=projects)


@portfolio.route('/<int:project_id>/')
def project(project_id):
	"""Returns a single project by its ID"""
	return "This is the work piece {}".format(project_id)


@portfolio.route('/add/')
@login_required
def addProject():
	"""Add a portfolio project"""
	form = ProjectForm()
	return render_template('portfolio/add.html', form=form)


@portfolio.route('/<int:project_id>/edit/')
@login_required
def editProject(project_id):
	"""Edit an existing portfolio project"""
	project = Project.query.get(project_id)
	form = ProjectForm()
	form.title.data = project.title
	form.description.data = project.description
	form.stack.data = project.stack
	form.stack.github_url = project.project_url
	return render_template('portfolio/edit.html', form=form)
