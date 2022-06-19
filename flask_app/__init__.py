from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import (
    LoginManager,
    current_user,
    login_user,
    logout_user,
    login_required,
)
import os

from flask_app.login.routes import login_blueprint
from flask_app.homepage.routes import homepage_blueprint
from flask_app.experience.routes import experience_blueprint
from flask_app.projects.routes import projects_blueprint

db = MongoEngine()
login_manager = LoginManager()

# application factory
def create_app():
    app = Flask(__name__)

    # db = MongoEngine()
    # login_manager = LoginManager()

    app.config["MONGODB_HOST"] = os.getenv("mongodb_uri")
    db.init_app(app)
    login_manager.init_app(app)

    # //// registering blueprints ////////////////////
    blueprints = [
        login_blueprint,
        homepage_blueprint,
        experience_blueprint,
        projects_blueprint
    ]
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
    # ////////////////////////////////////////////////

    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.objects(username=user_id).first()

    return app