from app import  db
from wtforms import FlaskForm
from datetime import datetime

class Country(db.model):
    country_id = db.Column('id',Integer(),primary_key= True),
    name = db.Column('name',String(30))


class   Film (db.model):
    id = db.Column('id',Integer(),primary_key= True)
    release_date = db.Column('realease_date',Integer())
    title = db.Column('title',String()),
    country_id = db.Column(db.Integer,db.Foreign_key('country.country_id'))
    created_in_country =db.relationship('country',backref = 'category',lazy = 'dynamic')
    available_in_countries = db.relationship('category',secondary = category ,back_populates = 'country')
    director = db.relationship('category',secondary = category ,back_populates = 'country')

class Director(db.model):
    id = db.Column('id',Integer, primary_key =True)
    first_name = db.Column('first_name',String())
    last_name = db.Column('last_name',String())







