from flask_wtf import Form
from wtforms import (TextField, StringField, BooleanField,PasswordField,
                    validators)

from .utils import Unique
from .models import User
from .constants import (USER_LEN_MSG, USER_REQ_MSG, USER_DUPL_MSG,
                        EMAIL_FORMAT_MSG, EMAIL_REQ_MSG, EMAIL_DUPL_MSG,
                        PWD_REQ_MSG, PWD_LEN_MSG, PWD_MATCH_MSG, INCORRECT_PWD)

class LoginForm(Form):
    username = TextField('Username',
                         [validators.Length(max=25,message=USER_LEN_MSG),
                            validators.Required(message=USER_REQ_MSG)])
    password = PasswordField('Password',
                            [validators.Required(message=PWD_REQ_MSG)])

class SignupForm(Form):

    username = TextField('Username', [validators.Length(max=25,
                                                        message=USER_LEN_MSG),
                          validators.Required(message=USER_REQ_MSG),
                          Unique(User,User.username, message=USER_DUPL_MSG)])
    email = TextField('Email', [validators.Email(message=EMAIL_FORMAT_MSG),
                    validators.Required(message=EMAIL_REQ_MSG),
                    Unique(User, User.email, message=EMAIL_DUPL_MSG)])
    password = PasswordField('Password', [validators.Length(max=25,
                                                          message=PWD_REQ_MSG),
                           validators.InputRequired(message=PWD_REQ_MSG),
                           validators.EqualTo('confirm',
                                              message=PWD_MATCH_MSG)])
    confirm = PasswordField('Repeat Password')

