from flask import Blueprint, redirect, render_template, url_for
from app.models import Project, Post
from .forms import ProjectForm
from flask_login import current_user, login_required
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
        project.owner = current_user.id
        form.populate_obj(project)
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('portfolio.home'))

    return render_template('portfolio/compose.html', form=form)


@portfolio.route('/<int:project_id>/edit/', methods=['GET', 'POST'])
@login_required
def editProject(project_id):
    """Edit an existing portfolio project"""
    project = Project.query.get(project_id)
    # Check that user is the owner of the project (not necessary atm)
    if current_user.id != project.owner:
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
