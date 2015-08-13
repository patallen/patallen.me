from flask import Flask
from flaskext.markdown import Markdown
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_envvar('PATALLENME_SETTINGS')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
Markdown(app, extensions=['fenced_code', 'codehilite', 'tables'])
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'adminbp.login'

# Import Blueprint
from app.admin.views import adminbp
from app.blog.views import blog
from app.portfolio.views import portfolio
from app.about.views import about

# Register blueprints
app.register_blueprint(adminbp)
app.register_blueprint(blog)
app.register_blueprint(portfolio)
app.register_blueprint(about)
