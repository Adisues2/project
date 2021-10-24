import os

from postgress.postgress import app

basedir = os.path.abspath(os.path.dirname(__file__))


	db_info = {'host': 'localhost',
			   'database': 'bookstore',
			   'psw': '1234',
			   'user': 'postgres',
			   'port': ''}

class Config:
		SECRET_KEY = "B&E)H@McQeThWmZq"
   app.config[
		'SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}@{db_info['host']}/{db_info['database']}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

