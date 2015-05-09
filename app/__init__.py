from flask import Flask
from app.admin.views import admin
from app.blog.views import blog
from app.work.views import work

app = Flask(__name__)

# Register blueprints
app.register_blueprint(admin)
app.register_blueprint(blog)
app.register_blueprint(work)

from app import views
