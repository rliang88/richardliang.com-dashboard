from flask import (
    Blueprint,
    render_template
)

from ..models import User

experience_blueprint = Blueprint("experience", __name__)

@experience_blueprint.route("/experience")
def index():
    return render_template("experience.html")