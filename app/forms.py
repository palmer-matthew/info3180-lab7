from typing import Text
from flask_wtf import FlaskForm 
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields import TextAreaField
from wtforms.validators import Email,DataRequired, InputRequired

class UploadForm(FlaskForm):

    description = TextAreaField('Description', validators=[DataRequired()])
    photo = FileField('Photo Upload', validators= [FileRequired(), FileAllowed(['jpg','png','Images only!'])])
