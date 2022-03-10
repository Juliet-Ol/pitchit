
from app.main import bp
from app import db

from flask import render_template,redirect, url_for, flash
from app.main.forms import PitchForm
from app.models import  Pitch
from flask_login import current_user

#views
@bp.route('/', methods = ['GET','POST'])
@bp.route('/pitch', methods = ['GET', 'POST'])
def index():
    form = PitchForm()
    if form.validate_on_submit():
        pitch = Pitch(content=form.content.data, author=current_user)
        db.session.add(pitch)
        db.session.commit()
        flash('Your pitch has been added', 'success')
        return redirect(url_for('main.index'))      
    pitches = Pitch.query.order_by(Pitch.timestamp.desc()).all()    
    return render_template ('index.html',title = 'home', form=form, pitches=pitches)


      