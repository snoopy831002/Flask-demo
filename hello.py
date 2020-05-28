from flask import Flask
from flask import render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

class User2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

@app.route('/', methods=['GET','POST'])
def hello_world():
    if(request.method == 'POST'):
        # save data
        username = request.form['username']
        email = request.form['email']
        user = User2(id=1,username=username,email
                     =email)
        db.session.add(user)
        db.session.commit()
        return "Updated"


    else:
        return render_template("test.html")


@app.route('/hello')
def hello():
    return "hello"

@app.route('/hello/<int:userid>')
def hello_userid(userid):
    return "hello "+url_for("hello")