from datetime import datetime

from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from flask_login import current_user, login_required

from flask_app.common.forms import (
    CreateContentForm,
    CreateLinkForm,
    UpdateContentForm,
    UpdateLinkForm,
)
from flask_app.models import (
    Experience,
    ExperienceBullet,
    ExperienceLink,
    ExperienceTechnology,
    HomepageDetailsLink,
    load_user,
)
from flask_app.utils import current_time

common_blueprint = Blueprint(
    "common", __name__, url_prefix="/common", template_folder="./templates"
)

# note: even though Bullet and Technology are conceptually
# the same - both of them are just text, we can't combine them into the same
# model since then it would be impossible to retreive a certain experience
# or project's bullets and technology seperately.
link_collections = [HomepageDetailsLink, ExperienceLink]
bullet_collections = [ExperienceBullet]


@common_blueprint.route(
    "/create_link/<link_model>",
    methods=["GET", "POST"],
    defaults={"related_document_creation_date": None},
)
@common_blueprint.route(
    "/create_link/<link_model>/<related_document_creation_date>",
    methods=["GET", "POST"],
)
@login_required
def create_link(link_model, related_document_creation_date=None):
    create_link_form = CreateLinkForm()

    if create_link_form.validate_on_submit():
        new_link = None

        # CASE: HomepageDetails
        if link_model == "HomepageDetailsLink":
            new_link = HomepageDetailsLink(
                owner=load_user(current_user.username),
                link_name=create_link_form.link_name.data,
                url=create_link_form.url.data,
                creation_time=current_time(),
            )

        # CASE: Experience
        elif link_model == "ExperienceLink":
            related_experience = Experience.objects(
                owner=load_user(current_user.username),
                creation_time=related_document_creation_date,
            ).first()

            new_link = ExperienceLink(
                owner=load_user(current_user.username),
                link_name=create_link_form.link_name.data,
                url=create_link_form.url.data,
                creation_time=current_time(),
                experience=related_experience,
            )

        new_link.save()
        return redirect(session["url"])

    return render_template(
        "create_link.html",
        form=create_link_form,
        title=f"Create Link Form - {link_model}",
    )


@common_blueprint.route("/update_link/<link_creation_time>", methods=["GET", "POST"])
@login_required
def update_link(link_creation_time):
    link = None
    for link_collection in link_collections:
        link = link_collection.objects(
            owner=load_user(current_user.username), creation_time=link_creation_time
        ).first()

        if link is not None:
            break

    if link is None:
        # TODO: return 404
        pass

    update_link_form = UpdateLinkForm(link_name=link.link_name, url=link.url)

    if update_link_form.validate_on_submit():
        link.update(
            link_name=update_link_form.link_name.data, url=update_link_form.url.data
        )

        return redirect(session["url"])

    return render_template(
        "update_link.html", form=update_link_form, title="Update Link Form"
    )


@common_blueprint.route("/delete_link/<link_creation_time>", methods=["GET", "POST"])
@login_required
def delete_link(link_creation_time):
    link = None
    for link_collection in link_collections:
        link = link_collection.objects(
            owner=load_user(current_user.username), creation_time=link_creation_time
        ).first()

        if link is not None:
            break

    if link is None:
        # TODO: return 404
        pass

    link.delete()

    return redirect(session["url"])


@common_blueprint.route(
    "/create_bullet/<bullet_model>/<related_document_creation_date>",
    methods=["GET", "POST"],
)
@login_required
def create_bullet(bullet_model, related_document_creation_date):
    create_bullet_form = CreateContentForm()

    if create_bullet_form.validate_on_submit():
        new_bullet = None

        if bullet_model == "ExperienceBullet":
            related_experience = Experience.objects(
                owner=load_user(current_user.username),
                creation_time=related_document_creation_date,
            ).first()

            new_bullet = ExperienceBullet(
                owner=load_user(current_user.username),
                creation_time=current_time(),
                experience=related_experience,
                content=create_bullet_form.content.data,
            )
        elif bullet_model == "ExperienceTechnology":
            related_experience = Experience.objects(
                owner=load_user(current_user.username),
                creation_time=related_document_creation_date,
            ).first()

            new_technology = ExperienceTechnology(
                owner=load_user(current_user.username),
                creation_time=current_time(),
                experience=related_experience,
                tech=create_bullet_form.content.data,
            )
        # TODO: 2nd case - Projects Bullet

        new_bullet.save()
        return redirect(session["url"])

    return render_template(
        "create_bullet.html",
        form=create_bullet_form,
        title=f"Create Link Form - {bullet_model}",
    )


@common_blueprint.route(
    "/update_bullet/<bullet_creation_time>", methods=["GET", "POST"]
)
@login_required
def update_bullet(bullet_creation_time):
    bullet = None
    for bullet_collection in bullet_collections:
        bullet = bullet_collection.objects(
            owner=load_user(current_user.username), creation_time=bullet_creation_time
        ).first()

        if bullet is not None:
            break

    if bullet is None:
        # TODO: return 404
        pass

    update_bullet_form = UpdateContentForm(content=bullet.content)

    if update_bullet_form.validate_on_submit():
        bullet.update(content=update_bullet_form.content.data)

        return redirect(session["url"])

    return render_template(
        "update_bullet.html", form=update_bullet_form, title="Update Bullet Form"
    )


@common_blueprint.route(
    "/delete_bullet/<bullet_creation_time>", methods=["GET", "POST"]
)
@login_required
def delete_bullet(bullet_creation_time):
    bullet = None
    for bullet_collection in bullet_collections:
        bullet = bullet_collection.objects(
            owner=load_user(current_user.username), creation_time=bullet_creation_time
        ).first()

        if bullet is not None:
            break

    if bullet is None:
        # TODO: return 404
        pass

    bullet.delete()

    return redirect(session["url"])


@common_blueprint.route(
    "/create_technology/<technology_model>/<related_document_creation_date>",
    methods=["GET", "POST"],
)
@login_required
def create_technology(technology_model, related_document_creation_date):
    create_technology_form = CreateContentForm()

    if create_technology_form.validate_on_submit():
        new_technology = None

        if technology_model == "ExperienceTechnology":
            related_experience = Experience.objects(
                owner=load_user(current_user.username),
                creation_time=related_document_creation_date,
            ).first()

            new_technology = ExperienceTechnology(
                owner=load_user(current_user.username),
                creation_time=current_time(),
                experience=related_experience,
                tech=create_technology_form.content.data,
            )

        new_technology.save()
        return redirect(session["url"])
    return render_template(
        "create_technology.html",
        form=create_technology_form,
        title=f"Create Technology Form - {technology_model}",
    )
