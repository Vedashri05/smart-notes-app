from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,Regexp

class RegistrationForm(FlaskForm):
    username=StringField("username",validators=[DataRequired(message="Enter username, cannot be empty!"),
        Regexp(r'^[A-Za-z_]+$', # Only letters and _ allowed
               message="Username can contain only letters and underscore")
        ])
    email=EmailField("email",validators=[DataRequired(),Email()])
    password=PasswordField("password",validators=[DataRequired(),
        Length(min=6,message="Password should be of minimum 6 charachter")])
    submit=SubmitField("Register")

class LoginForm(FlaskForm):
    username=StringField("username",validators=[DataRequired(message="Enter username, cannot be empty!"),
        Regexp(r'^[A-Za-z_]+$', # Only letters and _ allowed
               message="Username contain only letters and underscore")
        ])
    password=PasswordField("password",validators=[DataRequired(),
        Length(min=6,message="Password should be of minimum 6 charachter")])
    remember_me = BooleanField('Remember me')
    submit=SubmitField("Login")