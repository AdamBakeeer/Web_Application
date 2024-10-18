from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms import StringField
from wtforms.validators import DataRequired

class PropertyForm(FlaskForm):
    address = StringField('Address', validators=[DataRequired()])
    duration = IntegerField('duration', validators=[DataRequired()])
    rent = IntegerField('rent', validators=[DataRequired()])