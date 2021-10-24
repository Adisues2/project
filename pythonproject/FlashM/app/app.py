from flask import Flask, flash, render_template, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = "you-will-never-guess"


@app.route('/')
def index():
    # flash("This is a flashed message.")
    return redirect(url_for('example'))


@app.route("/example")
def home():
    flash("This is a flashed message.")
    return render_template("home.html")


@app.route("/page")
def page():
    flash("Error", "error")
    flash("Logged in successfully", "success")
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
