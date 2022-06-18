from flask import (
    Blueprint,
    render_template
)

from ..models import User

projects_blueprint = Blueprint("projects", __name__)

@projects_blueprint.route("/projects")
def index():
    return render_template("projects.html")