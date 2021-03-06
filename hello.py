from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello_name():
    return '<p>index page!</p>'

@app.route('/hello')
def hello_world():
    return '<p>hello world</p>'

@app.route('/user/<username>')
def show_user_profile(username):
    #show the user profile for that user
    return f'User: { escape(username) }'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    #show the post within a given id, the id is a integer
    return f'Post: { post_id }'

@app.route('/path/<path:subpath>')
def show_path(subpath):
    #show the path after /path/
    return f'Subpath: { escape(subpath) }'

@app.route('/login')
def login():
    return 'login'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login',next='/'))
    print(url_for('user', usename='John Doe'))
