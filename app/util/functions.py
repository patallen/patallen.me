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
