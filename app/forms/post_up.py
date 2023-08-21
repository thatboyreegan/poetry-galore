from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField
from wtforms.validators import InputRequired, Length


class PostUpform(FlaskForm):
    title = StringField('Title', validators=[InputRequired(),
                                             Length(min=4, max=100)])
    poem_b = TextAreaField('Body of the poem', validators=[InputRequired(),
                                                           Length(max=1024)])
    author = StringField('Author', validators=[InputRequired(),
                                               Length(min=1, max=1000)])
