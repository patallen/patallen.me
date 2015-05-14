from flask_wtf import Form
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired, URL


class ProjectForm(Form):
	"""WTForm for creating/editing portfolio project"""
	title = StringField('Title', validators=[DataRequired()])
	description = TextAreaField('Description', validators=[DataRequired()])
	stack = StringField('Stack')
	github_url = StringField('Github', validators=[URL()])
	image = FileField('Image')