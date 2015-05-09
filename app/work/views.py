from flask import Blueprint
from flask import render_template 

work = Blueprint('work', __name__, url_prefix='/work')


@work.route('/')
def home():
    return render_template('work/home.html')


@work.route('/<int:work_id>')
def piece(work_id):
    return "This is the work piece {}".format(work_id)
