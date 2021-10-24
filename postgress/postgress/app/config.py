import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = "B&E)H@McQeThWmZq"
	SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir, 'app.db') # postgresql://<username>:<password>@localhost/<database name>
	SQLALCHEMY_TRACK_MODIFICATIONS = False

