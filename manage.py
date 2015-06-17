from app import app, db
from app.models import User
from commands import CreateSuperuser
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('createsuperuser', CreateSuperuser())

if __name__ == '__main__':
    manager.run()
