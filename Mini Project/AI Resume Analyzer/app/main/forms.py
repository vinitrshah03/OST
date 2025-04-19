from flask_wtf import FlaskForm
from wtforms import FileField, StringField, SubmitField
from wtforms.validators import DataRequired

class ResumeForm(FlaskForm):
    resume = FileField('Resume', validators=[DataRequired()])
    job_title = StringField('Job Title', validators=[DataRequired()])
    submit = SubmitField('Submit')
