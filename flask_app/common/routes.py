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
    HomepageDetails,
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