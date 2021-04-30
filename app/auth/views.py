from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user,login_required,logout_user,current_user
from ..models import User
from .forms import LoginForm,RegistrationForm
from .. import db
from . import auth

@auth.route('/login',methods=['GET','POST'])
def login():
  
    if current_user.is_authenticated:
        return redirect(url_for('main.index')) 
      
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        
        if user is not None and user.verify_password(form.password.data):
            next_page = request.args.get('next')
         
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
            flash('User logged in', 'success')
        
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')

    title = "Sign In"
    return render_template('auth/login.html',form = form,title=title)
  
@auth.route('/register',methods = ["GET","POST"])
def register():
  
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
                        
    form = RegistrationForm()
    
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        
        db.session.add(user)
        db.session.commit()
        
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('auth.login'))
      
        title = "Create Account"
    return render_template('auth/register.html',form = form)
  
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))




  
 
  


  