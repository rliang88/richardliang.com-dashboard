from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for
)
from flask_login import(
    login_required,
    current_user
)
from flask_app.models import (
    HomepageDetails, 
    load_user
)
from flask_app.homepage.forms import (
    RealNameUpdateForm
)

homepage_blueprint = Blueprint("homepage", __name__, url_prefix='/homepage', template_folder='./templates')

def matching_username(username):
    return current_user.username == username

@homepage_blueprint.route("/")
@login_required
def index():
    homepage_details = HomepageDetails.objects(
        owner=load_user(current_user.username)
    ).first()

    return render_template(
        "homepage.html", 
        title=f"{current_user.username}\'s homepage",
        homepage_details = homepage_details
    )

@homepage_blueprint.route("/update_real_name", methods=["GET", "POST"])
@login_required
def update_real_name():
    full_name_update_form = RealNameUpdateForm()
    if full_name_update_form.validate_on_submit():
        homepage_details = HomepageDetails.objects(owner=current_user)
        homepage_details.update(real_name = full_name_update_form.full_name.data)

        return redirect(url_for('homepage.index'))
    
    return render_template("update_real_name.html", form=full_name_update_form, title="Update Full Name")