from flask_wtf import Form
from wtforms import StringField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired, URL, Optional


class ProjectForm(Form):
    """WTForm for creating/editing portfolio project"""
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    blog_post = SelectField('Blog Post', validators=[Optional()])
    stack = StringField('Stack')
    github_url = StringField('Github URL', validators=[Optional(), URL()])
    live_url = StringField('Live URL', validators=[Optional(), URL()])
    order_num = IntegerField('Order Number')
    image_url = StringField('Image URL', validators=[URL()])
