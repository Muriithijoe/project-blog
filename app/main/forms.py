from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required
class BlogForm(FlaskForm):
    title = StringField('Enter blog title',validators=[Required()])
    description= TextAreaField('blog')
    submit = SubmitField('Submit')
class CommentForm(FlaskForm):
    comment = TextAreaField('Enter comment.',validators = [Required()])
    submit = SubmitField('Submit')
class SubscriberForm(FlaskForm):
    email = StringField("Email Address",validators=[Required(),Email()])
    submit = SubmitField("Subscribe")

    def validate_email(self,data_field):
        if Subscriber.query.filter_by(email =data_field.data).first():
            raise ValidationError("Account already subscribed with that email")

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
