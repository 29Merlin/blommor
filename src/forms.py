from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class SearchForm(FlaskForm):
    search = StringField('Search', validators=[
        DataRequired(message='Search query cannot be empty'),
        Length(min=1, max=100, message='Search must be between 1 and 100 characters')
    ])
    submit = SubmitField('Search')