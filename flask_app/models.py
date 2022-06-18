from flask_login import UserMixin
from . import db

class User(db.Document, UserMixin):
    username = db.Stringfield(required=True, unique=True)
    password = db.Stringfield(required=True)

    def get_id(self):
        return self.username