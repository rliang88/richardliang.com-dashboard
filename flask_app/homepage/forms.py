from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    TextAreaField
)
from wtforms.fields import (
    URLField
)
from wtforms.validators import (
    InputRequired
)

class RealNameUpdateForm(FlaskForm):
    full_name = StringField("Full Name", validators=[InputRequired()])
    update = SubmitField("Update")

class PFPLinkUpdateForm(FlaskForm):
    url = URLField(
        "Image URL (ending in .jpg, .png, etc...",
        validators = [InputRequired()]
    )
    update = SubmitField("Update")

class DescriptionUpdateForm(FlaskForm):
    description = TextAreaField("Description", validators=[InputRequired()])
    update = SubmitField("Update")

class PersonalLinkUpdateForm(FlaskForm):
    link_name = StringField("Link Name", validators=[InputRequired()])
    url = URLField("Link URL", validators=[InputRequired()])
    update = SubmitField("Update")

class PersonalLinkAddForm(FlaskForm):
    link_name = StringField("Link Name", validators=[InputRequired()])
    url = URLField("Link URL", validators=[InputRequired()])
    submit = SubmitField("Add")

class AboutMeUpdateForm(FlaskForm):
    about_me = TextAreaField("About Me", validators=[InputRequired()])
    update = SubmitField("Update")