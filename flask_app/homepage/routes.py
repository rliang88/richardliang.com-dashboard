from flask import (
    Blueprint,
    render_template
)
from flask_login import(
    login_required,
    current_user
)
from flask_app.models import (
    HomepageDetails, 
    load_user
)

homepage_blueprint = Blueprint("homepage", __name__, url_prefix='/homepage')

@homepage_blueprint.route("/")
@login_required
def index():
    homepage_details = HomepageDetails.objects(
        owner=load_user(current_user.username)
    ).first()
    
    return render_template(
        "homepage.html", title=f"{current_user.username}\'s homepage"
    )