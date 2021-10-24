import flask

from app import app
from app import  routes



@app.route("/")
def index():
    posts = [
        {"author":"John", "body":"I love python"},
        {"author":"Fish", "body":"I love water"},
        {"author":"Herpetolog", "body":"I love pythons"},
    ]
    return flask.render_template('index.html',posts=posts)

