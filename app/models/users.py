from .. import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

def _create(username, email):
    user = User(id=1, username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return

def _update(id, email):
    user = User.query.filter_by(id=id).first()
    user.email = email
    db.session.commit()
    return

def _destroy(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return

def __init__(self, username = None, email = None):
        self.username = username
        self.email = email

def __repr__(self):
        return '<User %r>' % self.username