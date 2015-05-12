from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='admin.login'

# Import Blueprints 
from app.admin.views import admin
from app.blog.views import blog
from app.portfolio.views import portfolio
# Register blueprints
app.register_blueprint(admin)
app.register_blueprint(blog)
app.register_blueprint(portfolio)


from app import views
