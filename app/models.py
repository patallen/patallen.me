from sqlalchemy import event
from datetime import datetime
from markdown import markdown
from app import helpers
import re
import bcrypt
from app import db
from sqlalchemy.ext.hybrid import hybrid_property

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(60), unique=True)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60))
    date_created = db.Column(db.DateTime, default=db.func.now())
    location = db.Column(db.String(60))
    authenticated = db.Column(db.Boolean(), default=True)
    pw_hash = db.Column(db.String(60))

    @hybrid_property
    def password(self):
        return self.pw_hash

    @password.setter
    def _set_pass(self, password):
        password_salt = bcrypt.gensalt()
        self.pw_hash = bcrypt.hashpw(password.encode('utf-8'), password_salt)

    def validate_pass(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), self.pw_hash) == self.pw_hash

    def is_active(self):
        return True

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(240), nullable=False)
    body_md  = db.Column(db.String(), nullable=False)
    body_html = db.Column(db.String())
    excerpt = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, default=db.func.now())
    date_updated = db.Column(db.DateTime, onupdate=db.func.now())


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(100))
    description = db.Column(db.String(500))
    stack = db.Column(db.String())
    project_url = db.Column(db.String())
    img_url = db.Column(db.String())
    date_completed = db.Column(db.Date)


@event.listens_for(Post.body_md, 'set')
def _generate_html(target, value, *unused):
    target.body_html = markdown(value)
    target.excerpt = helpers.getExcerpt(target.body_html, 240)
