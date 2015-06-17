from app import db
from app.models import User
from flask_script import Command, prompt, prompt_pass


class CreateSuperuser(Command):
    """Creates the Superuser"""

    def run(self):
        username = prompt('Enter a username')
        first_name = prompt('Enter your first name')
        last_name = prompt('Enter your last name')
        password = prompt_pass('Enter password')
        confirm_pass = prompt_pass('Enter your password again')

        if password == confirm_pass:
            try:
                user = User()
                user.nickname = username
                user.first_name = first_name
                user.last_name = last_name
                user.password = password
                db.session.add(user)
                db.session.commit()
                print "User {} created successfully.".format(username)
            except:
                print "Could not create user. Try a different username."
        else:
            print "Passwords do not match, try again."
