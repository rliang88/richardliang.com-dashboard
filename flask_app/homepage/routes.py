from flask import (
    Blueprint,
    render_template
)
from flask_login import(
    login_required
)


homepage_blueprint = Blueprint("homepage", __name__)

@homepage_blueprint.route("/homepage")
@login_required
def index():
    return render_template("homepage.html")