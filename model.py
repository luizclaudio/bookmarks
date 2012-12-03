from google.appengine.ext import db
#from datetime import datetime

class User(db.Model):
    name = db.StringProperty(required = True)
    email = db.StringProperty(required = True)
    password = db.StringProperty(required = True)
    status = db.StringProperty(required = True, choices = set(['new', 'active', 'suspended']))
    created = db.DateTimeProperty(auto_now_add = True)
    #created = db.DateTimeProperty(default = datetime.fromtimestamp())

class Tag(db.Model):
    name = db.StringProperty(required = True)
    lower = db.StringProperty(required = True)
    user = db.ReferenceProperty(User, collection_name = 'tags')

class Bookmark(db.Model):
    title = db.StringProperty(required = True)
    link = db.StringProperty(required = True)
    user = db.ReferenceProperty(User, collection_name = 'bookmarks')

class BookmarkTag(db.Model):
    bookmark = db.ReferenceProperty(Bookmark, required = True, collection_name = 'bookmarks')
    tag = db.ReferenceProperty(Tag, required = True, collection_name = 'tags')
