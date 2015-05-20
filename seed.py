from app import db
from app.models import *

categories=[
        {"name": "Projects"},{"name": "News"},{"name": "Life"}
]

def deleteAll():
    for user in User.query.all():
        db.session.delete(user)
        db.session.commit()

    for project in Project.query.all():
        db.session.delete(project)
        db.session.commit()

    for post in Post.query.all():
        db.session.delete(post)
        db.session.commit()

    for cat in Category.query.all():
        db.session.delete(cat)
        db.session.commit()

def createUser():
    p = User()
    p.nickname = "Pat"
    p.first_name = "Patrick"
    p.last_name = "Allen"
    p.location = "Windham, NH"
    p.password = "password"
    
    db.session.add(p)
    db.session.commit()


def createCategories():
    for cat in categories:
        db.session.add(Category(cat['name']))
        db.session.commit()

if __name__ == '__main__':
    deleteAll()
    createUser()
    createCategories()
