from flask import Blueprint, redirect, render_template, url_for
from app.models import Project
from .forms import ProjectForm
from flask_login import current_user, login_required
from app import db

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


@portfolio.route('/add/', methods=['GET', 'POST'])
@login_required
def addProject():
	"""Add a portfolio project"""
	form = ProjectForm()

	if form.validate_on_submit():
		project = Project()
		project.owner = current_user.id
		project.title = form.title.data
		project.description = form.description.data
		project.stack = form.stack.data
		project.project_url = form.github_url.data
		db.session.add(project)
		db.session.commit()

		return redirect(url_for('portfolio.project', project_id=project.id))

	return render_template('portfolio/add.html', form=form)


@portfolio.route('/<int:project_id>/edit/', methods=['GET', 'POST'])
@login_required
def editProject(project_id):
	"""Edit an existing portfolio project"""
	project = Project.query.get(project_id)
	# Check that user is the owner of the project (not necessary atm)
	if current_user.id != project.owner:
		return "You do not have permission to edit this project."

	form = ProjectForm()

	if form.validate_on_submit():
		project.title = form.title.data
		project.description = form.description.data
		project.stack = form.stack.data
		project.project_url = form.github_url.data
		db.session.add(project)
		db.session.commit()

		return redirect(url_for('portfolio.project', project_id=project.id))

	# Pre-populate form with existing data
	form.title.data = project.title
	form.description.data = project.description
	form.stack.data = project.stack
	form.github_url.data = project.project_url

	return render_template('portfolio/edit.html', form=form, project_id=project_id)
