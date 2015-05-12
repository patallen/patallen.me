import os

base_dir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'patallen.db')

SECRET_KEY = "ThisISMYSECRETKEY"
