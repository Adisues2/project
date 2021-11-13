import flask
from app1 import app


@app.route('/home')
def home():
    posts = [
        {"author": "john", "body": "i love python"},
        {"author": "Fish", "body": "i love water"},
        {"author": "Herpetolog", "body": "i love python"},
    ]
    return flask.render_template('home.html', posts=posts)
