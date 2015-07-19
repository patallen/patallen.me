from sqlalchemy import event
from datetime import datetime
from markdown import markdown
from app import helpers
import re
from app import bcrypt
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
    pw_hash = db.Column(db.String())

    @hybrid_property
    def password(self):
        return self.pw_hash

    @password.setter
    def _set_pass(self, password):
        self.pw_hash = bcrypt.generate_password_hash(password)

    def validate_pass(self, password):
        return bcrypt.check_password_hash(self.pw_hash, password)

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
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    slug = db.Column(db.String(), unique=True)
    title = db.Column(db.String(240), nullable=False)
    body_md  = db.Column(db.String(), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.now())
    date_updated = db.Column(db.DateTime, onupdate=db.func.now())
    category = db.relationship('Category')

    def __init__(self, author, category_id, title, body_md):
        self.title = title
        self.category_id = category_id
        self.author = author
        self.body_md = body_md
        self.slug = helpers.createSlug(title)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(100))
    description = db.Column(db.String(500))
    stack = db.Column(db.String(1000))
    github_url = db.Column(db.String(1000))
    live_url = db.Column(db.String(1000))
    img_url = db.Column(db.String(300))
    date_completed = db.Column(db.Date)
    order_num = db.Column(db.Integer, default=0)
    # TODO: Add blog_slug to link to related blog post



class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(240))
    name = db.Column(db.String(60), nullable=False)
    slug = db.Column(db.String(), unique=True)

    def __unicode__(self):
        return self.slug
