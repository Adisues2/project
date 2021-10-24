from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField
from wtforms.validators import input_required, Length


class LoginForm(FlaskForm):
    firstname = StringField('firstname', validators=[input_required(), Length(min=4, max=15)])
    lastname = StringField('lastname', validators=[input_required(), Length(min=8, max=80)])
    age = IntegerField('age ', validators=[input_required(), Length(min=4, max=15)])
    experiences = StringField('experiences', validators=[input_required(), Length(min=4, max=15)])
    submit = [SubmitField('validate_on_submit()')]

