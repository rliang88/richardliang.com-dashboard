from datetime import datetime
from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash
)
from flask_login import(
    login_required,
    current_user
)
from flask_app.models import (
    HomepageDetailsLink,
    load_user,
    Link
)
from flask_app.homepage.forms import (
    FullNameUpdateForm,
    PFPLinkUpdateForm,
    DescriptionUpdateForm,
    PersonalLinkAddForm,
    PersonalLinkUpdateForm,
    AboutMeUpdateForm,
    EmailUpdateForm
)

common_blueprint = Blueprint(
    "common", __name__, url_prefix="/common", template_folder="./templates"
)

def matching_username(username):
    return current_user.username == username

@homepage_blueprint.route(
    "/update_link/<link_owner_username>/<link_creation_time>", methods=["GET", "POST"]
)
@login_required
def update_link(link_owner_username, link_creation_time):
    if not matching_username(link_owner_username):
        flash("You can\'t edit someone else\'s link!")
        return redirect(url_for('homepage.index'))
    
    link_collections = [HomepageDetailsLink]
    
    link = None
    for link_collection in link_collections:
        link = link_collection.objects(
            owner=load_user(link_owner_username),
            creation_time = link_creation_time
        ).first()

        if link is not None:
            break
    