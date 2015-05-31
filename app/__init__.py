from flask import Flask
from flaskext.markdown import Markdown
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_envvar('PATALLENME_SETTINGS')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
Markdown(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='admin.login'

# Import Blueprints 
from app.admin.views import admin
from app.blog.views import blog
from app.portfolio.views import portfolio
from app.about.views import about 
# Register blueprints
app.register_blueprint(admin)
app.register_blueprint(blog)
app.register_blueprint(portfolio)
app.register_blueprint(about)
