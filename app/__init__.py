from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../patallendb.db'
db = SQLAlchemy(app)

# Import Blueprints 
from app.admin.views import admin
from app.blog.views import blog
from app.portfolio.views import portfolio
# Register blueprints
app.register_blueprint(admin)
app.register_blueprint(blog)
app.register_blueprint(portfolio)


from app import views
from app.blog import views
