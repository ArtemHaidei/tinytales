from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from app.constants import UserType


class SignUpForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name')
    email = EmailField('Email', validators=[DataRequired(), Email()])
    user_type = SelectField('Register as', choices=[UserType.READER.value, UserType.AUTHOR.value], default=UserType.READER)
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=50)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Sign Up')


class SignInForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


