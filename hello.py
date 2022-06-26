from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello_name():
    return '<p>index page!</p>'

@app.route('/hello')
def hello_world():
    return '<p>hello world</p>'

