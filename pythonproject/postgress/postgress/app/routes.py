import flask

from app import app, db
from app.model import Book


@app.route('/')
def index():
	return flask.render_template('index.html')

@app.route('/add_book/<id>/<title>')
def add_book(id, title):
	book = Book(book_id=id, title=title)
	db.session.add(book)
	db.session.commit()

@app.route('/update_book_title/<int:id>/<title>')
def update_book(id, title):
	book = Book.query.filter_by(book_id=id).first()
	book.title = title
	db.session.add(book)
	db.session.commit()

@app.route('/update_expired_books_title/<int:id>/<title>')
def update_expired_books(id, title):
	book = Book.query.filter_by(book_id=id).first()
	book.title = title
	db.session.expire(book) # the add and commit will not change anything at the database after the expire
	db.session.add(book)
	db.session.commit()

@app.route('/refresh_book/<int:id>/<title>')
def refresh_book(id, title):
	book = Book.query.filter_by(book_id=id).first()
	book.title = title
	db.session.refresh(book) # refreshing means to expire and then immediately get the latest data for the object from the database. but it gets it fro the memory or from the transaction buffer
	book.title = title + 'here'
	db.session.add(book)
	db.session.commit()

# Expire - I persisted some changes for an object to the database. I don't need this updated object anymore in the current method, but I don't want any subsequent methods to accidentally use the wrong attributes.
# Refresh - I persisted some changes for an object to the database. I need to use this updated object within the same method.