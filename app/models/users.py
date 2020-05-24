from .. import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

def create(user):
    db.session.add(user)
    db.session.commit()
    return

def __init__(self, username = None, email = None):
        self.username = username
        self.email = email

def __repr__(self):
        return '<User %r>' % self.username