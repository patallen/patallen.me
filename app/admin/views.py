from flask import Blueprint

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/')
def adminhome():
    return "This is the admin page"


@admin.route('/signin/')
def adminsignin():
    return "Sign in as admin here"
