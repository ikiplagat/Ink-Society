
from flask import Flask, render_template, url_for, flash, redirect, abort, request
from . import main
from ..models import User, Post
from flask_login import login_required, current_user
from .forms import PostForm
from .. import db, photos

@main.route("/", methods = ['GET'])
def home():
    post = Post.query.order_by(Post.date.desc()).all()
    
    return render_template('home.html', title='Home', posts=post)


@main.route("/about")
def about():
    return render_template('about.html', title='About')


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/create_post',methods = ['GET','POST'])
@login_required
def create_post():
    title = 'create_post'
    form = PostForm()
    print(form.errors)
    
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        user_id = current_user._get_current_object().id
        
        new_post = Post(title = title,content=content,user_id = user_id)
        
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("main.home"))
    
    return render_template('create_post.html', title = title, form = form)




