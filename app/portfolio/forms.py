from flask_wtf import Form
from wtforms import StringField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired, URL, Optional


class ProjectForm(Form):
    """WTForm for creating/editing portfolio project"""
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    stack = StringField('Stack')
    github_url = StringField('Github URL', validators=[Optional(), URL()])
    live_url = StringField('Live URL', validators=[Optional(), URL()])
    img_url = StringField('Image URL', validators=[URL()])
    order_num = IntegerField('Order Number')
    blog_post_id = SelectField('Blog Post', validators=[Optional()], coerce=int)
