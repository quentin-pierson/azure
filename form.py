from wtforms import Form, SelectMultipleField, StringField, TextAreaField, RadioField, SubmitField, validators
from flask_wtf import FlaskForm

class Research(FlaskForm):
    tags = SelectMultipleField("Choose a tags", validate_choice=False)
    type = RadioField('type', [validators.Length(min=4, max=25)])
    description = TextAreaField('description', [validators.optional(), validators.length(max=200)])
    target = StringField('target', [validators.Length(min=4, max=25)])
    format = RadioField('format', [validators.Length(min=4, max=25)])
    submit = SubmitField('Submit')


class Upload(Form):
    pass