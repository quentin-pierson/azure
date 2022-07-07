from flask_wtf.file import FileRequired, FileAllowed
from wtforms import SelectMultipleField, RadioField, TextAreaField, StringField, SubmitField, FileField, validators
from flask_wtf import FlaskForm

class Research(FlaskForm):
    tags = SelectMultipleField("Choose a tags", validate_choice=False)
    # type = RadioField('type', choices=["Logo", "Humain", "Produit"])
    # description = TextAreaField('description', [validators.optional(), validators.length(max=200)])
    # target = RadioField('target', choices=["Traiteur", "Fast Food", "Finger Food", "Brasserie"])
    submit = SubmitField('Submit')


class Upload(FlaskForm):
    image = FileField('Image File', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Submit')