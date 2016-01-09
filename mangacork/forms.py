from flask_wtf import Form
from wtforms import (TextField, StringField, BooleanField,PasswordField,
                    validators)

from .utils import Unique
from .models import User

class LoginForm(Form):
    user_len_msg = 'Username is too long'
    user_req_msg = 'Username must be filled'
    pwd_req_msg = 'Password must be filled'
    username = TextField('Username',
                         [validators.Length(max=25,message=user_len_msg),
                            validators.Required(message=user_req_msg)])
    password = PasswordField('Password',
                            [validators.Required(message=pwd_req_msg)])

class SignupForm(Form):
    user_len_msg = 'Username cannot be longer than 25 characters'
    user_req_msg = 'Username must be filled'
    user_dupl_msg = 'Username is already taken'
    email_format_msg = 'Invalid email format'
    email_req_msg = 'Email must be filled'
    email_dupl_msg = 'Email is already taken'
    pwd_req_msg = 'Password must be filled'
    pwd_len_msg = 'Password cannot be longer than 25 characters'
    pwd_match_msg = 'Passwords must match'

    username = TextField('Username', [validators.Length(max=25,
                                                        message=user_len_msg),
                          validators.Required(message=user_req_msg),
                          Unique(User,User.username, message=user_dupl_msg)])
    email = TextField('Email', [validators.Email(message=email_format_msg),
                    validators.Required(message=email_req_msg),
                    Unique(User, User.email, message=email_dupl_msg)])
    password = PasswordField('Password', [validators.Length(max=25,
                                                          message=pwd_req_msg),
                           validators.InputRequired(message=pwd_req_msg),
                           validators.EqualTo('confirm',
                                              message=pwd_match_msg)])
    confirm = PasswordField('Repeat Password')

