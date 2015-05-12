from flask import Blueprint, render_template, redirect, url_for
from .forms import LoginForm
from app.models import User
from flask.ext.login import login_user, logout_user, current_user
from app import login_manager

admin = Blueprint('admin', __name__, url_prefix='/admin')

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@admin.route('/login/', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		nickname = form.nickname.data
		password = form.password.data
		user = User.query.filter_by(nickname=nickname).first()
		if user and user.validate_pass(password):
			login_user(user)
			return redirect(url_for('home'))
	return render_template('admin/login.html', form=form)


@admin.route('/logout/')
def logout():
	logout_user()
	return redirect(url_for('home'))
