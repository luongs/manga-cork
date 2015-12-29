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
    page = db.Column(db.String(80), nullable=False)
    chapter = db.Column(db.String(80), nullable=False)

    def __init__(self, comment, page, chapter):
        self.comment = comment
        self.page = page
        self.chapter = chapter

    def __repr__(self):
        return '<Comment {}>'.format(self.comment)
