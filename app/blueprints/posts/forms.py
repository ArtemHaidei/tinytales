from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
from app.constants import PostStatus


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=3, max=50)])
    content = TextAreaField('Content', validators=[DataRequired(), Length(min=3, max=500)])
    status = SelectField('Status', choices=[status.value for status in PostStatus if status != PostStatus.DELETED], default=PostStatus.DRAFT.value)
    slug = StringField('Slug', validators=[DataRequired(), Length(min=3, max=255)])
    submit = SubmitField('Create')