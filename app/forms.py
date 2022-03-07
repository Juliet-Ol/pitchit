from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,SubmitField
from wtforms.validators import DataRequired, Length,Email,Regexp, EqualTo

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(1, 32)])
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField(
        'Password', 
        validators=[DataRequired()],
        render_kw=('placeholder', 'Enter password')
        )
    confirm_password = PasswordField(
        'Confirm password',
        validators =[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register') 