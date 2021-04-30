from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required
from ..models import User


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Home'
    
    return render_template('index.html', title = title)

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/create_post',methods = ['GET','POST'])
@login_required
def create_post():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'create_post'
    form = PostForm()
    print(form.errors)
    if form.is_submitted():
        print('submitted')
    if form.validate():
        print("valid")
    print(form.errors)
    
    if form.validate_on_submit():
        title = form.title.data
        user_id = current_user._get_current_object().id
        content = form.content.data
        new_post = Post(title = title,content=content,user_id = user_id)
        
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("main.index"))
    
    return render_template('create_post.html', title = title, form = form)


