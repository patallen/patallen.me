from app import db
from app.models import Category, Post, Project

categories = [
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

projects = [
    {
        'owner': 1,
        'title': 'Markdraft.com',
        'description': 'Markdown document revision control system. Save your markdown documents as you write them. Revert back to previous versions if needed.',
        'stack': 'Django, jQuery, Angular, Postgres',
        'github_url': 'http://github.com/patallen/markdraft.com/',
        'live_url': '',
        'img_url': 'http://i.imgur.com/Q3C1poB.png',
        'order_num': 3
    },
    {
        'owner': 1,
        'title': 'snip.space',
        'description': 'Ad-free, free, and open source code and text snippet repository.',
        'stack': 'Flask, Celery, Postgres',
        'github_url': 'http://github.com/patallen/snip.space/',
        'live_url': 'http://snip.space/',
        'img_url': 'http://i.imgur.com/MZtiNo0.png',
        'order_num': 2
    },
    {
        'owner': 1,
        'title': 'patallen.me',
        'description': 'My personal website. Features include blogging in markdown and a portfolio page. You are on it right now.. :)',
        'stack': 'Flask, Postgres',
        'github_url': 'http://github.com/patallen/patallen.me/',
        'live_url': 'https://patallen.me',
        'img_url': 'http://i.imgur.com/FWdDcMB.png',
        'order_num': 1
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


def createProjects():
    for proj in projects:
        db.session.add(Project(**proj))
    db.session.commit()


if __name__ == '__main__':
    deleteAll()
    createCategories()
    createProjects()
