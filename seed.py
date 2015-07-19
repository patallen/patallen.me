from app import db
from app.models import *

categories=[
{
    'name': 'Projects',
    'slug': 'projects'
},
{
    'name': 'Code',
    'slug': 'code'
},
{
    'name': 'Random',
    'slug': 'random'
}
]

def deleteAll():
    for project in Project.query.all():
        db.session.delete(project)
        db.session.commit()

    for post in Post.query.all():
        db.session.delete(post)
        db.session.commit()

    for cat in Category.query.all():
        db.session.delete(cat)
        db.session.commit()


def createCategories():
    for cat in categories:
        name = cat['name']
        slug = cat['slug'] 
        db.session.add(Category(name=name, slug=slug))
        db.session.commit()

if __name__ == '__main__':
    deleteAll()
    createCategories()
