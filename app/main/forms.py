from flask_wtf import FlaskForm
# from flask_wtf.recaptcha import validators
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Length, Required


class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[
                           Required(), Length(1, 128)])
    email = StringField("Email", validators=[Required()])
    password = PasswordField("Password", validators=[Required()])
    submit = SubmitField("Sign Up")


class SignInForm(FlaskForm):
    username = StringField("Username", validators=[Required()])
    password = PasswordField("Password", validators=[Required()])
    remember = BooleanField("Remember Me?")
    submit = SubmitField("Sign in")
