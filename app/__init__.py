from flask import Flask
from app.admin.views import admin
from app.blog.views import blog
from app.portfolio.views import portfolio

app = Flask(__name__)

# Register blueprints
app.register_blueprint(admin)
app.register_blueprint(blog)
app.register_blueprint(portfolio)

from app import views
