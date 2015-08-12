from app import app
from flask import render_template


class NoPostsFound(Exception):
    pass


class InvalidCategory(Exception):
    pass


class ResourceNotFound(Exception):
    pass


class Unauthorized(Exception):
    pass


@app.errorhandler(NoPostsFound)
def no_posts_found(e):
    """Custom errorhandler that renders a '404
    no posts found' error template."""
    return render_template('errorpages/404.html', message=e), 404


@app.errorhandler(InvalidCategory)
def invalid_category(e):
    """Custom errorhandler that renders a '404
    invalid category' error template."""
    return render_template('errorpages/404.html', message=e), 404


@app.errorhandler(ResourceNotFound)
def post_not_found(e):
    """Custom errorhandler that renders a '404
    resource not found' error template."""
    return render_template('errorpages/404.html', message=e), 404


@app.errorhandler(Unauthorized)
def unauthorized(e):
    """Custom errorhandler that renders a '401
    unauthorized' error template."""
    return render_template('errorpages/401.html', message=e), 401
