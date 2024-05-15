from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from gamemoguls.models import Users

class RegistrationForm(FlaskForm):
    """
    Form for user registration
    """
    username = StringField('Username', validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email', validators=[DataRequired(), Email(),Length(max=60)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6,max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

class LoginForm(FlaskForm):
    """
    Form for user login
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Login')

class resetPasswordForm(FlaskForm):
    """
    Form for user reset password
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Reset Password')

    def validate (self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('If an account exists with that email, a reset link has been sent to your email')
        
class newPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6,max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    resetPassword = SubmitField('Reset Password')