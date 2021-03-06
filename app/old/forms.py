from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
# from app.models import User

#class LoginForm(FlaskForm):
#    username = StringField('Username', validators=[DataRequired()])
#    password = PasswordField('Password', validators=[DataRequired()])
#    remember_me = BooleanField('Remember Me')
#    submit = SubmitField('Sign In')

# user login form
class LoginForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

# admin register form
# class RegistrationForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     password2 = PasswordField(
#         'Repeat Password', validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Register')

#     def validate_username(self, username):
#         user = User.query.filter_by(username=username.data).first()
#         if user is not None:
#             raise ValidationError('Please use a different username.')

#     def validate_email(self, email):
#         user = User.query.filter_by(email=email.data).first()
#         if user is not None:
#             raise ValidationError('Please use a different email address.')

# # admin login form
# class AdminLoginForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     submit = SubmitField('Sign In')

# # admin reset_pass form
# class ResetPassForm(FlaskForm):
#     password = PasswordField('New Password', validators=[DataRequired()])
#     password2 = PasswordField(
#         'Confirm Password', validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Reset Password')