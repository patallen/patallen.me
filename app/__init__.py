from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from app.admin.views import admin
from app.blog.views import blog
from app.portfolio.views import portfolio

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../patallendb.db'
db = SQLAlchemy(app)

# Register blueprints
app.register_blueprint(admin)
app.register_blueprint(blog)
app.register_blueprint(portfolio)

from app import views
