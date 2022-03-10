
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired



class PitchForm(FlaskForm):
    content = TextAreaField('Pitch', validators=[DataRequired()])
    submit = SubmitField('Submit')    