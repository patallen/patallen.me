from flask import Blueprint
from flask import render_template 

portfolio = Blueprint('portfolio', __name__, url_prefix='/portfolio')


@portfolio.route('/')
def home():
    return render_template('portfolio/home.html')


@portfolio.route('/<int:project_id>')
def project(project_id):
    return "This is the work piece {}".format(project_id)
