from flask import Flask
from flask import render_template, url_for

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def hello_world():
    return render_template("test.html")


@app.route('/hello')
def hello():
    return "hello"

@app.route('/hello/<int:userid>')
def hello_userid(userid):
    return "hello "+url_for("hello")