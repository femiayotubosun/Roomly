from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, FileField, TextAreaField
from wtforms.validators import Length, Required


class ProfileForm(FlaskForm):
    name = StringField("Name", validators=[Length(1, 128)])
    address = StringField("Address", validators=[Required()])
    school = StringField("School", validators=[Required()])
    email = StringField("Email", validators=[Required()])
    number = StringField("Phone No", validators=[Required()])
    gender = SelectField('Gender', choices=[
                         '--Select your gender--', 'Male', 'Female'])
    about = TextAreaField("About me")
    photo = FileField('File')
    submit = SubmitField("Update Profile")
