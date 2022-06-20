from flask import (
    Blueprint,
    render_template
)
from flask_login import(
    login_required
)


projects_blueprint = Blueprint("projects", __name__)

@projects_blueprint.route("/projects")
@login_required
def index():
    return render_template("projects.html")