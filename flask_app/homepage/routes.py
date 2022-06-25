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
    FullNameUpdateForm,
    PFPLinkUpdateForm,
    DescriptionUpdateForm
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

@homepage_blueprint.route("/update_full_name", methods=["GET", "POST"])
@login_required
def update_full_name():
    full_name_update_form = FullNameUpdateForm()
    if full_name_update_form.validate_on_submit():
        homepage_details = HomepageDetails.objects(owner=current_user).first()
        homepage_details.update(full_name = full_name_update_form.full_name.data)

        return redirect(url_for('homepage.index'))
    
    return render_template(
        "update_full_name.html", form=full_name_update_form, title="Update Full Name"
    )

@homepage_blueprint.route("/update_pfp_link", methods=["GET", "POST"])
@login_required
def update_pfp_link():
    pfp_link_update_form = PFPLinkUpdateForm()

    if pfp_link_update_form.validate_on_submit():
        homepage_details = HomepageDetails.objects(owner=current_user).first()
        homepage_details.update(pfp_link = pfp_link_update_form.url.data)

        return redirect(url_for('homepage.index'))
    
    return render_template(
        "update_pfp_link.html", form=pfp_link_update_form, title="Homepage - Update PFP Link"
    )

@homepage_blueprint.route("/update_description", methods=["GET", "POST"])
@login_required
def update_description():
    homepage_details = HomepageDetails.objects(owner=current_user).first()

    description_update_form = DescriptionUpdateForm(
        description = homepage_details.description
    )

    if description_update_form.validate_on_submit():
        homepage_details.update(description = description_update_form.description.data)

        return redirect(url_for('homepage.index'))
    
    return render_template(
        "update_description.html", form=description_update_form, title="Homepage - Update Description"
    )