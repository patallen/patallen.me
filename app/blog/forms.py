from flask_wtf import Form
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class PostForm(Form):
	"""WTForm for creating/editing blog post"""
	title = StringField('Title', validators=[DataRequired()])
	body = TextAreaField('Body', validators=[DataRequired()])
	category = SelectField('Category', validators=[DataRequired()], coerce=int)
