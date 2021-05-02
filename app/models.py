from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    posts = db.relationship('Post', backref='user', lazy=True)
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    comment = db.relationship('Comment',backref='post',lazy='dynamic')

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    def delete_post(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_post(cls,id):
        post=Post.query.filter_by(id=id).first()
        return post

    def __repr__(self):
        return f"Post('{self.title}'"
    
    
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text(),nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id'),nullable = False)

    def save_c(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_comment(self):
        db.session.delete(self)
        db.session.commit()    

    @classmethod
    def get_comments(cls,post_id):
        comments = Comment.query.filter_by(post_id=post_id).all()

        return comments

    
    def __repr__(self):
        return f'comment:{self.comment}' 
    
    
class Quote:
  '''
  Quote class that defines the quotes instances
  '''
  def __init__(self,id,author,quote):

    self.id=id
    self.author=author
    self.quote=quote           