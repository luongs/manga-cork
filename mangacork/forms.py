from flask_wtf import Form
from wtforms import (TextField, StringField, BooleanField,PasswordField,
                    validators)

from .utils import Unique
from .models import User

class LoginForm(Form):
    user_len_msg = 'Username is too long'
    user_req_msg = 'Username must be filled'
    pwd_req_msg = 'Password must be filled'
    username = TextField('username',
                         [validators.Length(max=25,message=user_len_msg),
                            validators.Required(message=user_req_msg)])
    password = StringField('password',
                            [validators.Required(message=pwd_req_msg)])

class SignupForm(Form):
    user_len_msg = 'Username cannot be longer than 25 characters'
    user_req_msg = 'Username must be filled'
    pwd_req_msg = 'Password must be filled'
    pwd_len_msg = 'Password cannot be longer than 25 characters'
    pwd_match_msg = 'Passwords must match'
    username = TextField('username', [validators.Length(max=25,
                                                        message=user_len_msg),
                          validators.Required(message=user_req_msg),
                          Unique(User,User.username,message='Username taken')])
    password = StringField('password', [validators.Length(max=25,
                                                          message=pwd_req_msg),
                           validators.InputRequired(message=pwd_req_msg),
                           validators.EqualTo('confirm',
                                              message=pwd_match_msg)])
    confirm = PasswordField('Repeat Password')

