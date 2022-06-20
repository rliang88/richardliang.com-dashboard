from flask import (
    Blueprint,
    render_template
)
from flask_login import(
    login_required
)

experience_blueprint = Blueprint("experience", __name__)

@experience_blueprint.route("/experience")
@login_required
def index():
    return render_template("experience.html")