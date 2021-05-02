from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required
from ..models import Post
from wtforms import ValidationError
from flask_login import current_user
            
class PostForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    content = TextAreaField('Your Post', validators=[Required()])
    submit = SubmitField('Post')   
    
    def validate_post(self,data_field):
            if Post(title =data_field.data,content =data_field.data).first():
                raise ValidationError('Error in displaying post')
            

class CommentForm(FlaskForm):
    comment = TextAreaField('Post comment', validators=[Required()])
    submit = SubmitField('Submit')            