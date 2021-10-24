from app import db


class pets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    age = db.Column(db.Integer,unique =True)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))

    phonenumbers = db.relationship('Phonenumber', backref='person', lazy='dynamic')

    def __repr__(self):
        return f'<Person: {self.id}, {self.name}, {self.email}, {self.phonenumbers}>'


class Phonenumber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(64))

    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))

    def __repr__(self):
        return f'<Phonenumber: {self.id}, {self.number}, {self.person_id}>'
