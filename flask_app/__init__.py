from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

db = MongoEngine()
login_manager = LoginManager()
bcrypt = Bcrypt()

def nuke_collections():
    print("Nuking database...")
    for collection_name in db.get_db().list_collection_names():
        # collection is pymongo.collection.Collection
        collection = db.get_db()[collection_name]
        collection.delete_many({})
    print("done")

def seed_users():    
    print("populating users...")
    from .models import User

    hashed_password = bcrypt.generate_password_hash(os.getenv("default_pwd")).decode("utf-8")
    u1 = User(
        username=os.getenv("default_username"),
        password=hashed_password
    )
    u1.save()

    print("done")

def nuke_and_seed_users():
    nuke_collections()
    seed_users()

# application factory
def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.getenv("secret_key")
    app.config["MONGODB_HOST"] = os.getenv("mongodb_uri")
    
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    # need to import this as models.py is not implicitly imported
    from flask_app.models import load_user

    # // registering blueprints ////////////////////
    from flask_app.users.routes import users_blueprint
    from flask_app.homepage.routes import homepage_blueprint
    from flask_app.experience.routes import experience_blueprint
    from flask_app.projects.routes import projects_blueprint
    blueprints = [
        users_blueprint,
        homepage_blueprint,
        experience_blueprint,
        projects_blueprint
    ]
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
    # //////////////////////////////////////////////
    
    app.before_first_request(nuke_and_seed_users)

    login_manager.login_view = "users.login"
    
    return app