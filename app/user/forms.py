from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, FileField
from wtforms.validators import Length


class ProfileForm(FlaskForm):
    name = StringField("Name", validators=[Length(1, 128)])
    address = StringField("Address")
    school = StringField("School")
    email = StringField("Email")
    number = StringField("Phone No")
    gender = SelectField('Gender', choices=[
                         '--Select your gender--', 'Male', 'Female'])
    photo = FileField('File')
    submit = SubmitField("Update Profile")
