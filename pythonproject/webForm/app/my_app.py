
from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import input_required, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-never-will-guess'
Bootstrap(app)


class LoginForm(FlaskForm):
    username = StringField('username', validators=[input_required(), Length(min=4, max=15)])
    password = StringField('password', validators=[input_required(), Length(min=4, max=180)])
    remember = BooleanField('remember me')


@app.route('/')
def index():
    return "hello world"


# @app.route('/<name>')
# def display_username(name):
#     print(name)
#     return f"""
#     <html>
#     <head>
#     <title>
#     home page -microblog
#     </title>
#     </head>
#     <body>
#     <h1>hello ,{name.title}</h1>
#     </body>
#     </html>
#
#     """
#

@app.route('/')
def segnup_page():
    return render_template('signup.html')


# @app.route('/sign')
# def homepage():
#     return 'welcome'
#     return render_template('signup.html')


@app.route('/page', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return '<h1>' + form.username.data + " " + form.password.data + '<h1>'
    return render_template('page.html', form=form)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
