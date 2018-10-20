from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required
class PitchForm(FlaskForm):
    title = StringField('Enter pitch category',validators=[Required()])
    description= TextAreaField('pitch description')
    submit = SubmitField('Submit')
class CommentForm(FlaskForm):
    comment = TextAreaField('Enter comment.',validators = [Required()])
    submit = SubmitField('Submit')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
