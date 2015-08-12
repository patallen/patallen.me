from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired
from app.models import Category

def categories_factory():
    """
    Return a queryset that contains all categories -- 
    used in PostForm QuerySelectField
    """
    return Category.query.all()

class PostForm(Form):
	"""WTForm for creating/editing blog post"""
	title = StringField('Title', validators=[DataRequired()])
	body_md = TextAreaField('Body', validators=[DataRequired()])
	category = QuerySelectField('Category',
	                            query_factory=categories_factory,
	                            allow_blank=False)

class DeleteForm(Form):
	"""WTForm for deleting a blog post"""
	delete = SubmitField('DELETE')
