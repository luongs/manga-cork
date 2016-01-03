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

class RegistrationForm(Form):
    username = TextField('username', [validators.Length(min=4, max=25),
                          validators.Required(),
                          Unique(User,User.username,message='Username taken')])
    msg = 'Password must match'
    password = StringField('password', [validators.Length(min=4, max=25),
                           validators.InputRequired(),
                           validators.EqualTo('confirm', message=msg)])
    confirm = PasswordField('Repeat Password')

