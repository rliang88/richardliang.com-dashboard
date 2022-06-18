from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
import os

from flask_app.login.routes import login_blueprint
from flask_app.homepage.routes import homepage_blueprint
from flask_app.experience.routes import experience_blueprint
from flask_app.projects.routes import projects_blueprint
# from mongodb_test import mongodb_test

# db = MongoEngine()
# login_manager = LoginManager()

def mongodb_test():
    print("HELLO WORLD")

def create_app():
    app = Flask(__name__)

    db = MongoEngine()
    login_manager = LoginManager()

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

    # app.before_first_request(mongodb_test)

    return app