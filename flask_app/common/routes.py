from datetime import datetime
from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    request,
    session
)
from flask_login import(
    login_required,
    current_user
)
from flask_app.models import (
    HomepageDetailsLink,
    load_user
)
from flask_app.common.forms import (
    UpdateLinkForm
)

common_blueprint = Blueprint(
    "common", __name__, url_prefix="/common", template_folder="./templates"
)

def matching_username(username):
    return current_user.username == username

@common_blueprint.route(
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
    
    if link is None:
        # TODO: return 404
        pass

    update_link_form = UpdateLinkForm(
        link_name = link.link_name,
        url = link.url
    )

    if update_link_form.validate_on_submit():
        link.update(
            link_name = update_link_form.link_name.data,
            url = update_link_form.url.data
        )

        return redirect(session['url'])
    
    return render_template(
        "update_link.html", form=update_link_form, title="Update Link Form"
    )