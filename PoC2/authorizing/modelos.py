from enum import Enum
#from bson.json_util import default
from flask_mongoengine import MongoEngine

from json import JSONEncoder

db = MongoEngine()

class Role(Enum):
   ADMIN = 1
   SALUD = 2
   PROVE = 3
   def default(self, o):
            return o.__dict__
   
class User(db.Document):
    name = db.StringField(unique=True)
    password = db.StringField()
    role = db.EnumField(Role, default=Role.SALUD)

class ValidateResponse(db.Document):
    success = db.BooleanField()
    status = db.StringField()
    mensaje = db.StringField()