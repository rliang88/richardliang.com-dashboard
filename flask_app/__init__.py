from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return "Hello World! <h1>Hello World!<h1>"

    return app