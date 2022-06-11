from flask import Flask

from flask_app.login.routes import login_blueprint
from flask_app.homepage.routes import homepage_blueprint
from flask_app.experience.routes import experience_blueprint
from flask_app.projects.routes import projects_blueprint

def create_app():
    app = Flask(__name__)

    # @app.route('/')
    # def home():
    #     return "Hello World! <h1>Hello World!<h1>"

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