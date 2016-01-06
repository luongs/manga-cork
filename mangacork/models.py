import arrow

from mangacork import bcrypt,db

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
    username = db.Column(db.String(20), nullable=False)

    def __init__(self, comment, image_path, username):
        self.comment = comment
        self.image_path = image_path
        self.username = username

    def __repr__(self):
        return '<Comment {}>'.format(self.comment)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, index=True,
                         nullable=False)
    password = db.Column(db.String(180),nullable=False)
    email = db.Column(db.String(30), unique=True,nullable=False)
    registered_on = db.Column(db.DateTime)

    def __init__(self, username, plaintext, email):
        self.username = username
        self.password = bcrypt.generate_password_hash(plaintext)
        self.email = email
        self.registered_on = arrow.utcnow().datetime

    # Following methods required by WTForms
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return True

    def get_id(self):
        return unicode(self.id)

    # Password authentication
    def is_correct_password(self, plaintext):
        if bcrypt.check_password_hash(self.password, plaintext):
            return True
        return False

    def __repr(self):
        return '<Username {}>'.format(self.username)
