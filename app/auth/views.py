
from flask import Flask, render_template, url_for, flash, redirect, request
from .forms import RegistrationForm, LoginForm
from . import auth
from ..models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from .. import db
from ..email import mail_message


@auth.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        
        mail_message("Welcome to The Ink Society","email/welcome_user",user.email,user=user)
        
        flash('Your account has been created successfully! Please log in to continue.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html', title='Register', form=form)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('auth/login.html', title='Login', form=form)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))