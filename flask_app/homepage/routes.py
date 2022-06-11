from flask import (
    Blueprint,
    render_template
)

homepage_blueprint = Blueprint("homepage", __name__)

@homepage_blueprint.route("/")
def index():
    return render_template("homepage.html")