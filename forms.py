from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo



class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired() ,  Length(min=3, max=30)])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired() ,  Length(min=3, max=30)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired() ,  Length(min=3, max=30), EqualTo('password')])

    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired() ,  Length(min=3, max=30)])

    submit = SubmitField('Login')