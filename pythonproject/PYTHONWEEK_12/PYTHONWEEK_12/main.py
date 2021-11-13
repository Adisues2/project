from flask import flash,render_template
from flask import Flask
app =Flask(__name__)

@app.route('/messages')

def message():
    # flash("Error","error")
    # flash("submit succefull",
    #       "submit")
    return  f'hello world gdfgdafdfSE '



if __name__ == "__main__":
    app.run(debug=True,port=5000)