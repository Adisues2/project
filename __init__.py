
from flask import Flask
from flask import render_template, url_for, redirect, flash, session, logging, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, BooleanField, SubmitField, validators
from wtforms.validators import DataRequired, email
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import psycopg2

from app.forms import LoginForm
from app.models import profile, User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

app.config[
    'SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:12345@localhost/hackathon'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['DEBUG'] = True
# Database Representation
db = SQLAlchemy(app)
migrate = Migrate(app, db)
