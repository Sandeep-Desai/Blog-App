from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,Length,EqualTo

class RegistrationForm(FlaskForm):
    user_name=StringField("Username",validators=[DataRequired(),Length(max=20,min=5)])
    email=StringField("Email",validators=[DataRequired(),Email()])
    password=PasswordField("Password",validators=[DataRequired()])
    confirm_password=PasswordField("Confirm password",validators=[EqualTo("password"),DataRequired()])
    submit=SubmitField("SignUp")

class loginForm(FlaskForm):
    email=StringField("Email",validators=[DataRequired(),Email()])
    password=PasswordField("Password",validators=[DataRequired()])
    # confirm_password=PasswordField("Confirm password",validators=[EqualTo("password"),DataRequired()])
    submit=SubmitField("Login")