from flask_wtf import Form
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired


class PostForm(Form):
	"""WTForm for creating/editing blog post"""
	title = StringField('Title', validators=[DataRequired()])
	body = TextAreaField('Body', validators=[DataRequired()])
	category = SelectField('Category', validators=[DataRequired()], coerce=int)

class DeleteForm(Form):
	"""WTForm for deleting a blog post"""
	delete = SubmitField('DELETE')
