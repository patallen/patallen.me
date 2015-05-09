from flask import Flask
from app.admin.views import admin
from app.blog.views import blog

app = Flask(__name__)
db = SQLAlchemy(app)

# Register blueprints
app.register_blueprint(admin)
app.register_blueprint(blog)

from app import views
