import re
from math import ceil

class Pagination():
    def hasPrev(self):
        if self.page > 1:
            return True
        else:
            return False

    def hasNext(self):
        if self.page < self.numPages:
            return True
        else:
            return False

    def __init__(self, page, count, items_per_page):
        self.page = page
        self.numPages = ceil(count / items_per_page)


def getExcerpt(html, length):
    """Takes html, strips it, and returns truncated text based on length"""
    text = re.sub('<[^<]+?>', '', html)
    if len(text) <= length:
        return text 
    else:
        return ' '.join(text[:length+1].split(' ')[0:-1]) + '...' 