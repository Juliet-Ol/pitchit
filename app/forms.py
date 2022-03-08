import email
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,SubmitField
from wtforms.validators import DataRequired, Length,Email,Regexp, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired(),Email()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password',validators =[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register') 