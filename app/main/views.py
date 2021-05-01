
from flask import Flask, render_template, url_for, flash, redirect, abort
from . import main
from ..models import User
from flask_login import login_required
from .. import db

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html', title='Home')


@main.route("/about")
def about():
    return render_template('about.html', title='About')


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


