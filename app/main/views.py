
from flask import Flask, render_template, url_for, flash, redirect, abort, request
from . import main
from ..models import User, Post, Comment
from flask_login import login_required, current_user
from .forms import PostForm,CommentForm
from .. import db, photos
from ..request import get_quotes
from ..email import mail_message

@main.route("/", methods = ['GET'])
def home():
    page = request.args.get(('page', 1))
    quote=get_quotes()
    
    post = Post.query.order_by(Post.date.desc()).paginate(page=page, per_page=5)
    
    return render_template('home.html', title='Home', posts=post, quote=quote)


@main.route("/user/<string:username>", methods = ['GET'])
def user_post(username):
    page = request.args.get(('page', 1))
    user = User().query.filter_by(username=username).first_or_404()
    
    post = Post.query.filter_by(user=user)\
    .order_by(Post.date.desc())\
    .paginate(page=page, per_page=5)
    
    return render_template('user_post.html', title='User posts', posts=post, user=user)


@main.route("/about")
def about():
    return render_template('about.html', title='About')


@main.route('/account/<uname>')
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
        flash('Your post has been created!', 'success')
        return redirect(url_for("main.home"))
    
    return render_template('create_post.html', title = title, form = form, legend = 'New Post')


@main.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@main.route("/post/<int:post_id>/update", methods = ['POST','GET'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.user != current_user:
        abort(403)
        
    form = PostForm()  
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('main.post', post_id = post_id))
    
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title = 'Update Post', form = form, legend = 'Update Post')


@main.route('/post/<int:post_id>/delete', methods = ['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.user != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))


@main.route('/comment/<int:post_id>', methods = ['POST','GET'])
@login_required
def comment(post_id):
    form = CommentForm()
    post = Post.query.get(post_id)
    all_comments = Comment.query.filter_by(post_id = post_id).all()
    
    if form.validate_on_submit():
        comment = form.comment.data 
        post_id = post_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,post_id = post_id)
        new_comment.save_c()
        
        return redirect(url_for('.comment', post_id = post_id))
    
    return render_template('comment.html', form =form, post = post,all_comments=all_comments)



