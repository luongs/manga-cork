from flask_wtf import Form
from wtforms import (TextField, StringField, BooleanField,PasswordField,
                    validators)

from .utils import Unique
from .models import User

class LoginForm(Form):
    username = TextField('username', [validators.Length(min=4, max=25),
                                      validators.Required()])
    password = StringField('password', [validators.Length(min=4, max=25),
                                        validators.Required()])

class RegistrationForm(Form):
    username = TextField('username', [validators.Length(min=4, max=25),
                          validators.Required(),
                          Unique(User,User.username,message='Username taken')])
    msg = 'Password must match'
    password = StringField('password', [validators.Length(min=4, max=25),
                           validators.Required(),
                           validators.EqualTo('confirm', message=msg)])
    confirm = PasswordField('Repeat Password')

