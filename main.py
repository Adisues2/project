from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField
from wtforms.validators import InputRequired, Length
from flask_bootstrap import Bootstrap
from flask import request
import pandas as pd

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'you-will-never-guess'


class LoginForm(FlaskForm):
    firstname = StringField('firstname', validators=[InputRequired(), Length(min=5, max=20)])
    lastname = StringField('lastname', validators=[InputRequired(), Length(min=4, max=60)])
    Experiences = StringField('Experiences', validators=[InputRequired(), Length(min=10, max=100)])
    Age = IntegerField('Age', validators=[InputRequired(), Length(min=6, max=10)])
    submit = SubmitField('submit')


@app.route('/')
def index():
    return 'welocme '


@app.route('/pages')
def new_pages():
    form = LoginForm()

    if form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        Experiences = form.Experiences.data
        Age = form.Age.data
        print("here is what i got from thr form")
        print('firstname', firstname)
        print('lastname', lastname)
        print('Experiences', Experiences)
        print('Age', Age)

        return redirect('/index.html')
    return render_template('page.html', form=form)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
