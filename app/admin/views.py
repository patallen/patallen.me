from flask import Blueprint, render_template, redirect, url_for, request
from .forms import LoginForm
from app.models import User, Post, Category, Project
from flask.ext.login import login_user, logout_user, current_user
from app import login_manager, app, db
from flask_login import login_required
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


class AdminModelView(ModelView):
    """
    Subclasses ModelView to require authentication for
    accessing the admin panel for the specified Model
    """
    def is_accessible(self):
        return current_user.is_authenticated()

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('adminbp.login', next=request.url))


# Create Blueprint
adminbp = Blueprint('adminbp', __name__)

# Create flask-admin and add model views
admin = Admin(app, name='patallenme', template_mode='bootstrap3')

admin.add_view(AdminModelView(Category, db.session))
admin.add_view(AdminModelView(Post, db.session))
admin.add_view(AdminModelView(Project, db.session))


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@adminbp.route('/login/', methods=['GET', 'POST'])
def login():
    """Lets the user log in to create/edit posts
    and portfolio projects.
    """
    form = LoginForm()
    if form.validate_on_submit():
            nickname = form.nickname.data
            password = form.password.data
            user = User.query.filter_by(nickname=nickname).first()
            if user and user.validate_pass(password):
                    login_user(user)
                    return redirect(url_for('about.home'))
    return render_template('admin/login.html', form=form)


@adminbp.route('/logout/')
@login_required
def logout():
    """Log out and redirect home."""
    logout_user()
    return redirect(url_for('about.home'))
