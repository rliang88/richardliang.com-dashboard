from flask import (
    Blueprint,
    render_template
)

projects_blueprint = Blueprint("projects", __name__)

@projects_blueprint.route("/projects")
def index():
    return render_template("projects.html")