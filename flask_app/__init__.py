from flask import Flask

from flask_app.homepage.routes import homepage

def create_app():
    app = Flask(__name__)

    # @app.route('/')
    # def home():
    #     return "Hello World! <h1>Hello World!<h1>"

    # //// registering blueprints ////////////////////
    app.register_blueprint(homepage)
    # ////////////////////////////////////////////////

    return app