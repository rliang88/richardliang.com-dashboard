from flask import (
    Blueprint,
    render_template
)

from ..models import User

login_blueprint = Blueprint("login", __name__)

@login_blueprint.route("/login")
def login():
    return render_template("login.html")