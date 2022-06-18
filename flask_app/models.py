from flask_login import UserMixin
from flask import current_app as app

@app.login_manager.user_loader
def load_user(user_id):
    return User.objects(username=user_id).first()

class User(app.db.Document, UserMixin):
    username = app.db.Stringfield(required=True, unique=True)
    password = app.db.Stringfield(required=True)

    def get_id(self):
        return self.username