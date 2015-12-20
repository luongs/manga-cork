from . import db

class LastPage(db.Model):
    __tablename__ = 'lastpage'

    id = db.Column(db.Integer, primary_key=True)
    lastpage = db.Column(db.String(80), unique=True)

    def __init__(self, lastpage):
        self.lastpage = lastpage

    def __repr__(self):
        return '<Lastpage {}>'.format(self.lastpage)

