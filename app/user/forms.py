from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length


class ProfileForm(FlaskForm):
    name = StringField("Name", validators=[Length(1, 128)])
    address = StringField("Address")
    school = StringField("School")
    email = StringField("Email")
    number = StringField("Phone No")
    submit = SubmitField("Update Profile")
