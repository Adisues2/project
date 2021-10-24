from app import app
from flask import render_template


@app.errorhandler(404)
def error_404(error):
    return render_template('404_error.html'), 404


@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return render_template('page_not_found.html'), 404


if __name__ == "__main__":
    app.run(debug=1 ,port=8080)