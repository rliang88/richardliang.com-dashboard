from flask import (
    Blueprint,
    render_template
)
from flask_login import(
    login_required,
    current_user
)


projects_blueprint = Blueprint("projects", __name__, url_prefix="/projects")

@projects_blueprint.route("/")
@login_required
def index():
    return render_template(
        "projects.html", title=f"{current_user.username}\'s projects"
    )