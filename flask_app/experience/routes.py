from flask import (
    Blueprint,
    render_template
)
from flask_login import(
    login_required,
    current_user
)

experience_blueprint = Blueprint("experience", __name__, url_prefix="/experience")

@experience_blueprint.route("/")
@login_required
def index():
    return render_template(
        "experience.html", title=f"{current_user.username}\'s experience"
    )