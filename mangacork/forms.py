from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, validators


class LoginForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25),
                                      validators.Required()])
    password = StringField('password', [validators.Length(min=4, max=25),
                                        validators.Required()])

class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25),
                          validators.Required()])
    msg = 'Password must match'
    password = StringField('password', [validators.Length(min=4, max=25),
                           validators.Required(),
                           validators.EqualTo('confirm', message=msg])
    confirm = PasswordField('Repeat Password')

