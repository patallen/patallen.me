from flask import Blueprint, redirect, render_template, url_for, Response
from .forms import ProjectForm
from flask_login import current_user, login_required

from app.models import Project
from app.util.functions import get_or_404
from app import db

portfolio = Blueprint('portfolio', __name__, url_prefix='/portfolio')


@portfolio.route('/')
def home():
    """Main portfolio page - displays list of projects"""
    projects = Project.query.order_by(Project.order_num.desc()).all()
    return render_template('portfolio/home.html', projects=projects)


@portfolio.route('/add/', methods=['GET', 'POST'])
@login_required
def addProject():
    """Add a portfolio project"""
    form = ProjectForm()

    if form.validate_on_submit():
        project = Project()
        project.owner = current_user
        form.populate_obj(project)
        project.slug = project.title.lower()
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('portfolio.home'))

    return render_template('portfolio/compose.html', form=form)


@portfolio.route('/<int:project_id>/edit/', methods=['GET', 'POST'])
@login_required
def editProject(project_id):
    """Edit an existing portfolio project"""
    project = get_or_404(Project, id=project_id)

    # Check that user is the owner of the project (not necessary atm)
    if current_user != project.owner:
        return "You do not have permission to edit this project."

    # Create the form and set it's values based
    # on what is in the DB for the specified form
    form = ProjectForm(obj=project)

    if form.validate_on_submit():
        form.populate_obj(project)
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('portfolio.home'))

    return render_template('portfolio/compose.html',
                           form=form,
                           project_id=project_id)


@portfolio.route('/<int:project_id>', methods=['DELETE'])
@login_required
def delete_project(project_id):
    """View for deleting a project with an ajax delete method"""
    project = get_or_404(Project, id=project_id)

    if current_user != project.owner:
        return Response("You do not have permission to edit this project.",
                        status=401)

    db.session.delete(project)
    db.session.commit()

    return Response('Delete Successful.', status=200)
