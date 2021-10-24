from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random
import os
import psycopg2
# Flask Object
app = Flask(__name__)
app.config['SECRET_KEY'] = random._urandom(56)
app.config['DEBUG'] = True
os.system('set FLASK_APP=run.py')

# Database Connection
# db_info = {'host': 'localhost',
#            'database': 'bookstore',
#            'psw': '12345',
#            'user': 'postgres',
#            'port': ''}
# from  psycopg2 import  connect
#
# try:
#     connection = psycopg2.connect(user="postgres",
#                                   password="12345",
#                                   host="localhost",
#                                   port="8080",
#                                   database="bookstore")
#     cursor = connection.cursor()
#
#
# except (Exception, psycopg2.Error) as error:
#     print("Failed to insert record into mobile table", error)
#
#

# app.config[
# 'SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}@{db_info['host']}{db_info['password']}/{db_info['database']}"
app.config['SQLALCHEMY_DATABASE_URI'] =f'postgresql://postgres:12345@localhost/book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database Representation
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from app import models, routes
