from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from wtforms import IntegerField, StringField

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI '] = f'postgresql://postgres:12345@localhost/bookstore'
db = SQLAlchemy(app)


# def create_app():
#
# db.init_app(app)
#  return app

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))


def __init__(self, username, email):
    self.username = username
    self.email = email


def __repr__(self):
    return '<user %r>' % self.username


@app.route('/add')
def index():
    return "<h1> hello flask</h1>"


if __name__ == "__main__":
    app.run(debug=True, port=8080)
