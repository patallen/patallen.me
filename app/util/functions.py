from flask_login import current_user

from app.models import Post
from app.util.errors import ResourceNotFound



def get_or_404(model, **kwargs):
    """
    Generic get_or_404 function. Takes a model and a field and value
    to filter by. It either returns the obj if it exists, or raises a
    ResourceNotFound with a message based on the model's __name__
    """
    obj = model.query.filter_by(**kwargs).first()
    if obj is None:
        raise ResourceNotFound('{} cannot be found.'.format(model.__name__))
    return obj


def get_posts_query(category=None, published_only=False):
    """
    Return a query based on category provided and whether or not
    unpublished results should be shown. -- If published_only is true
    or the user is not logged in, unpublished results will not be
    returned.
    """
    query = Post.query

    if category:
        query = query.filter_by(category=category)

    if current_user.is_anonymous() or published_only:
        query = query.filter_by(published=True)

    return query
