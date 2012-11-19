from google.appengine.ext import db

class Categoria(db.Model):
    descricao = db.StringProperty() #required=True)

class Coisa(db.Model):
    nome = db.StringProperty()
    descricao = db.StringProperty()
    preco = db.FloatProperty()
    categoria = db.ReferenceProperty(Categoria)

class User(db.Model):
    name = db.StringProperty(required = True)
    email = db.StringProperty(required = True)
    password = db.StringProperty(required = True)
    status = db.StringProperty(required = True, choices = set(['new', 'active', 'suspended']))