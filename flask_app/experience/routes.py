from datetime import datetime

from flask import Blueprint, flash, redirect, render_template, session, url_for
from flask_login import current_user, login_required

from flask_app.experience.forms import CreateExperienceForm
from flask_app.models import (
    Experience,
    ExperienceBullet,
    ExperienceLink,
    ExperienceTechnology,
    load_user,
)
from flask_app.utils import current_time

experience_blueprint = Blueprint(
    "experience", __name__, url_prefix="/experience", template_folder="./templates"
)


@experience_blueprint.route("/")
@login_required
def index():
    experiences = Experience.objects()

    return render_template(
        "experience.html",
        title=f"{current_user.username}'s experiences",
        experiences=experiences,
    )


@experience_blueprint.route("/create_experience", methods=["GET", "POST"])
@login_required
def create_experience():
    create_experience_form = CreateExperienceForm()

    if create_experience_form.validate_on_submit():
        new_experience = Experience(
            owner=load_user(current_user.username),
            company_name=create_experience_form.company_name.data,
            position=create_experience_form.position.data,
            start_date=create_experience_form.start_date.data,
            end_date=create_experience_form.end_date.data,
            about=create_experience_form.about.data,
            creation_time=current_time(),
        )
        new_experience.save()

        return redirect(url_for("experience.index"))

    return render_template(
        "create_experience.html",
        title="Experience - Create Experience",
        form=create_experience_form,
    )


@experience_blueprint.route(
    "/view_experience/<experience_creation_time>", methods=["GET"]
)
@login_required
def view_experience(experience_creation_time):
    session["url"] = url_for(
        "experience.view_experience", experience_creation_time=experience_creation_time
    )

    experience = Experience.objects(
        owner=load_user(current_user.username), creation_time=experience_creation_time
    ).first()

    if experience is None:
        # TODO: return 404
        pass

    tech_stack = ExperienceTechnology.objects(experience=experience)
    bullet_points = ExperienceBullet.objects(experience=experience)
    links = ExperienceLink.objects(experience=experience)

    return render_template(
        "view_experience.html",
        title="Experience Details",
        experience=experience,
        tech_stack=tech_stack,
        bullet_points=bullet_points,
        links=links,
    )
