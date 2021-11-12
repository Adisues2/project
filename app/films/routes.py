from flask import Blueprint

films_Blueprint = Blueprint('films',__name__)


@films_Blueprint.routes('/')
def index():
    return '<h1>hello wolrd</h1>'
