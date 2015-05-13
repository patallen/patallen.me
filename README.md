# patallen.me
This is the repository for code for my personal website, patallen.me.

### Set up repo and environment

1. `git clone https://github.com/patallen/patallen.me`
1. `cd patallen.me`
1. `virtualenv venv && . venv/bin/activate` (python 3)
1. `pip install -r requirements.txt`

### Set up the database
Using flask-migrate, to manage database migrations. Currently using SQLite, but will be moving to postgresql.

1. `python manage.py db init`
1. `python manage.py db upgrade`
1. `python seed.py`

### Todo:
- [ ] Add/Edit portfolio views/templates
- [ ] Plan home page
- [ ] Static page views/templates
- [ ] Make everything Pretty
- [x] Set up flask-login w/ bcrypt
- [x] Set up models (User, Post, Project)
- [x] Blog home
- [x] Blog post add/edit functionality