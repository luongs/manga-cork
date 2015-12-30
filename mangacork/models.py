import arrow
from mangacork import db

class LastPage(db.Model):
    __tablename__ = 'lastpage'

    id = db.Column(db.Integer, primary_key=True)
    lastpage = db.Column(db.String(80), unique=True)

    def __init__(self, lastpage):
        self.lastpage = lastpage

    def __repr__(self):
        return '<Lastpage {}>'.format(self.lastpage)

class Comments(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(260), nullable=False)
    image_path = db.Column(db.String(160), nullable=False)

    def __init__(self, comment, image_path):
        self.comment = comment
        self.image_path = image_path

    def __repr__(self):
        return '<Comment {}>'.format(self.comment)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, index=True)
    password = db.Column(db.String(20))
    email = db.Column(db.String(30), unique=True)
    registered_on = db.Column(db.DateTime)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.registered_on = arrow.utcnow()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return True

    def get_id(self):
        return unicode(self.id)

    def __repr(self):
        return '<Username {}>'.format(self.username)
