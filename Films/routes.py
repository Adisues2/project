from flask import Flask,blueprints,render_template
from wtforms import StringField,IntegerField,fields,SubmitField
from wtforms.validators import DataRequired,Length,Optional
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect, CSRFError
from flask_wtf import FlaskForm

app  = Flask(__name__)
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = 'you-will-never-guess'
class AddFilmForm(FlaskForm):
    title =StringField('title',[DataRequired(Length(min=5,max=20))]),
    Release_date = IntegerField('Release_date',[DataRequired(Length(min=5,max=20))]),
    Category = StringField('Category',[Optional()]),
    Country = StringField('Country',[Optional()]),
    Submit = SubmitField()

class AddDirectorForm(FlaskForm):

    first_name = StringField('first_name',[DataRequired(Length(min=5,max=20))]),
    last_name =StringField('last_name',[DataRequired(Length(min=5,max=20))]),
    Film = StringField('film',[DataRequired(Length(min=5,max=20))])
    Submit  = SubmitField()




@app.route('/page')
def index ():
    return  render_template('homepage.html')


@app.route('/')
def home ():
    return render_template('navbar.html')

@app.route('/Add a Film')
def page ():
    form = AddFilmForm()

    return render_template('addFilm.html',form =form)

@app.route('/Add a Director')
def home_login():
    form  = AddDirectorForm()
    return render_template('addDirector.html',form =form)

@app.route('/AddDirectorForm')
def pages ():
    return render_template('navbar.html')

if __name__ == "__main__":
    app.run(debug=True,port=8080)