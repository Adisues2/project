from app import db

class Book(db.Model):
	book_id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(64))

	def __repr__(self):
		return f'<Book: {self.title}>'

class Reader(db.Model):
	reader_id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(64), nullable=False)
	last_name = db.Column(db.String(64), nullable=False)

	def __repr__(self):
		return f'<Reader: {self.reader_id}>'
