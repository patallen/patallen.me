from flask import Blueprint
from flask import render_template 

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/')
def adminhome():
    return render_template('admin/home.html')


@admin.route('/signin/')
def adminsignin():
    return "Sign in as admin here"
