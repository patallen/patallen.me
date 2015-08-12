from flask_wtf import Form
from wtforms import StringField, TextAreaField, IntegerField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, URL, Optional
from app.models import Category, Post


def project_posts():
    """
    Returns a queryset that contains all posts in the 'projects'
    category. -- This is used by the blog_post QuerySelectField
    in the ProjectForm
    """
    proj_cat = Category.query.filter_by(slug='projects').one()
    return Post.query.filter_by(category=proj_cat)


class ProjectForm(Form):
    """WTForm for creating/editing portfolio project"""
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    stack = StringField('Stack')
    github_url = StringField('Github URL', validators=[Optional(), URL()])
    live_url = StringField('Live URL', validators=[Optional(), URL()])
    img_url = StringField('Image URL', validators=[URL()])
    order_num = IntegerField('Order Number')
    blog_post = QuerySelectField('Blog Post',
                                 query_factory=project_posts,
                                 allow_blank=True)
