import re
from slugify import slugify

def getExcerpt(html, length):
    """Takes html, strips it, and returns truncated text based on length"""
    text = re.sub('<[^<]+?>', '', html)
    if len(text) <= length:
        return text 
    else:
        return ' '.join(text[:length+1].split(' ')[0:-1]) + '...'

def createSlug(title):
    return str(slugify(title))
