from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def hello_world(name=None):
    return render_template('test.html', name=name)
