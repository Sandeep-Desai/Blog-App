from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,TextAreaField
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

class create_post(FlaskForm):
    title=StringField("Title",validators=[DataRequired()])
    content=TextAreaField("Content",validators=[DataRequired()])
    submit=SubmitField("Post")
