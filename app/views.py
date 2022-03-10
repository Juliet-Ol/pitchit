import email
from app import app, db
from app import forms
from flask import render_template,redirect, session, url_for, flash
from app.forms import LoginForm, RegistrationForm, PitchForm
from .models import User, Pitch
from flask_login import current_user, login_user, logout_user, login_required

#views
@app.route('/', methods = ['GET','POST'])
@app.route('/pitch', methods = ['GET', 'POST'])
def index():
    form = PitchForm()
    if form.validate_on_submit():
        pitch = Pitch(content=form.content.data, author=current_user)
        db.session.add(pitch)
        db.session.commit()
        flash('Your pitch has been added', 'success')
        return redirect(url_for('index'))      
    pitches = Pitch.query.order_by(Pitch.timestamp.desc()).all()    
    return render_template ('index.html',title = 'home', form=form, pitches=pitches)


@app.route('/login', methods = ['GET', 'POST'])    
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash ('Invalid username or password')
            return redirect(url_for('login'))   
        login_user(user, remember=form.remember.data)   
        flash(f'Logged in as {user.username}')
        return redirect(url_for('index'))        
    return render_template('login.html', title='Login', form=form)

@app.route('/register', methods = ['GET', 'POST'])    
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {user.username}')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)   

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))         