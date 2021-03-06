from app.auth import bp
from app import db
from flask import render_template,redirect,  url_for, flash
from app.auth.forms import LoginForm, RegistrationForm
from ..models import User
from flask_login import current_user, login_user, logout_user
from ..email import mail_message
# import smtplib


@bp.route('/login', methods = ['GET', 'POST'])    
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.index'))
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash ('Invalid username or password')
            return redirect(url_for('auth.login'))   
        login_user(user, remember=form.remember.data)   
        flash(f'Logged in as {user.username}')
        return redirect(url_for('main.index'))        
    return render_template('login.html', title='Login', form=form)

@bp.route('/register', methods = ['GET', 'POST'])    
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {user.username}')

        mail_message("Welcome to pitchit","email/welcome_user",user.email,user=user)

        return redirect(url_for('auth.login'))

    return render_template('register.html', title='Register', form=form)   

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))   