from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, TextAreaField, SubmitField
from flask import request


class ContactForm(FlaskForm):
    name = TextField("Name")
    email = TextField("Email")
    subject = TextField("Subject")
    message = TextAreaField("Message")
    submit = SubmitField("Send")
