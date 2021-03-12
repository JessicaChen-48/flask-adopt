"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, Optional, URL

class AddPet(FlaskForm):
    """Adds a pet"""

    name = StringField(
        "Name",
        validators=[InputRequired()],
    )

    species = SelectField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],
    )

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    ) 

    age = SelectField(
        "Age",
        choices=[("baby", "Baby"), ("young", "Young"), ("adult", "Adult"), ("senior", "Senior")],
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional()]
    )


class EditPet(FlaskForm):
    """Edit a pet"""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],

    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional()]
    )

    available = BooleanField("Available?")