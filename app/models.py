from app import helpers, bcrypt, db
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

    def __unicode__(self):
        return self.nickname


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    slug = db.Column(db.String(), unique=True)
    title = db.Column(db.String(240), nullable=False)
    body_md = db.Column(db.String(), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.now())
    date_updated = db.Column(db.DateTime, onupdate=db.func.now())
    author = db.relationship('User')
    category = db.relationship('Category')

    def __init__(self, title=''):
        self.slug = helpers.createSlug(title)

    def __unicode__(self):
        return self.title


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    slug = db.Column(db.String(64))
    description = db.Column(db.String(500))
    stack = db.Column(db.String(1000))
    github_url = db.Column(db.String(1000))
    live_url = db.Column(db.String(1000))
    img_url = db.Column(db.String(300))
    order_num = db.Column(db.Integer, default=0)

    # Currently not used in forms
    date_completed = db.Column(db.Date)

    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    owner = db.relationship('User')

    # Each Project can have a related blog post
    blog_post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    blog_post = db.relationship('Post')


    def __unicode__(self):
        return self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(240))
    name = db.Column(db.String(60), nullable=False)
    slug = db.Column(db.String(), unique=True)

    def __unicode__(self):
        return self.name
