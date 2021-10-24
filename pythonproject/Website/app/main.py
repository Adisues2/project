import flask
from flask import Flask
from flask import request
from Website.forms import LoginForm

app = Flask(__name__)
# my_app.py.config["SECRET_KEY "] = "you-will-never-guess"
app.secret_key = 'you-will-never-guess'

# class LoginForm(FlaskForm):
#     firstname = wtforms.StringField("firstname")
#     lastname = wtforms.StringField("lastname")
#     age = wtforms.IntegerField("age")
#     experiences = wtforms.TextField("expereinces")
#     submit = wtforms.SubmitField("submit")


@app.route('/myform', methods=("GET", "POST"))
def myform_page():
    form = LoginForm()
    if form.validate_on_submit():  # Check if the form has been filled

        form.firstname.data  # Get
        form.lastname.data  # The
        form.age.data  # Data

        print("Here is what I got from the form:")
        print("username:", firstname)
        print("password:", lastname)
        print("bio:", age)
        # Do something with the data

        return flask.redirect('/')
    return flask.render_template_string('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
