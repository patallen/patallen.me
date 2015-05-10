import re

def getExcerpt(html, length):
    """Takes html, strips it, and returns truncated text based on length"""
    text = re.sub('<[^<]+?>', '', html)
    if len(text) <= length:
        return text 
    else:
        return ' '.join(text[:length+1].split(' ')[0:-1]) + '...' 
