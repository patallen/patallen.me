# patallen.me
This is the repository for code for my personal website, patallen.me.

### Set up repo and environment

1. `$ git clone https://github.com/patallen/patallen.me`
1. `$ cd patallen.me`
1. `$ virtualenv venv && . venv/bin/activate` (python 2.7)
1. `$ pip install -r requirements.txt`

### Set up the database
Using flask-migrate to manage database migrations. Currently using PostgreSQL.

1. `$ python manage.py db upgrade`
1. `$ python manage.py createsuperuser`
1. `$ python seed.py`

### Create and link PATALLENME_SETTINGS
1. create a `patallenme_settings.py` and place it somewhere
1. include `SQLALCHEMY_DATABASE_URI`, `SECRET_KEY`, and `DEBUG`
1. `export PATALLENME_SETTINGS=~/location/to/patallenme_settings.py`

### Todo:
- [ ] Add blog_slug field to Project model
- [ ] Use flask-admin as admin interface
- [ ] Views for projects/post deletion
- [ ] Hide post / save as draft functionality
- [ ] Create and add favicon
- [ ] Implement image uploads for projects
- [ ] Use flask-images for server-side resizing
- [ ] Make everything Pretty
- [x] Add and Edit buttons for projects when logged in
- [x] Add/Edit projects functionality
- [x] Add markdown editor.
- [x] Slugs for blog posts
- [x] Static page views/templates
- [x] Add and Edit buttons for posts when logged in
- [x] Add/Edit portfolio views/templates
- [x] Set up flask-login w/ bcrypt
- [x] Set up models (User, Post, Project)
- [x] Blog home
- [x] Blog post add/edit functionality
