from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    TextAreaField
)
from wtforms.fields import (
    URLField,
    EmailField
)
from wtforms.validators import (
    InputRequired,
    ValidationError
)

from flask_app.utils import is_url
import re


class BaseLinkForm(FlaskForm):
    link_name = StringField("Link Name", validators=[InputRequired()])
    url = URLField("Link URL", validators=[InputRequired()])

    def validate_url(form, field):
        if not is_url(field.data):
            raise ValidationError("URL must be formatted correctly")

class CreateLinkForm(BaseLinkForm):
    submit = SubmitField("Add")

class UpdateLinkForm(BaseLinkForm):
    update = SubmitField("Update")

class BaseContentForm(FlaskForm):
    content = StringField("Content", validators=[InputRequired()])

class CreateContentForm(BaseContentForm):
    submit = SubmitField("Add")

class UpdateContentForm(BaseContentForm):
    update = SubmitField("Update")