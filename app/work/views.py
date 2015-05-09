from flask import Blueprint

work = Blueprint('work', __name__, url_prefix='/work')


@work.route('/')
def workhome():
    return "This is the main work page"


@work.route('/<int:work_id>')
def blogpost(work_id):
    return "This is the work piece {}".format(work_id)
