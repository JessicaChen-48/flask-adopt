"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtfforms import Stringfield, SelectField, TextAreaField, BooleanField
from wtf.validators import InputRequired, Length, Optional

class AddPet(FlaskForm):
    """Adds a pet"""

    name = Stringfield(
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
