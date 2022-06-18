from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
import os

from flask_app.login.routes import login_blueprint
from flask_app.homepage.routes import homepage_blueprint
from flask_app.experience.routes import experience_blueprint
from flask_app.projects.routes import projects_blueprint

db = MongoEngine()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    app.config["MONGODB_HOST"] = os.getenv("mongodb_uri")
    db.init_app()
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

    return app