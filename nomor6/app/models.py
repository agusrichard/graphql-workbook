from . import db


class Name(db.Model):
	__tablename__ = 'names'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	id_work = db.Column(db.Integer, db.ForeignKey('works.id'))
	id_salary = db.Column(db.Integer, db.ForeignKey('categories.id'))

class Work(db.Model):
	__tablename__ = 'works'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	id_salary = db.Column(db.Integer, db.ForeignKey('categories.id'))
	names = db.relationship('Name', backref='name', lazy='dynamic')

class Category(db.Model):
	__tablename__ = 'categories'
	id = db.Column(db.Integer, primary_key=True)
	salary = db.Column(db.Integer)
	names = db.relationship('Name', backref='name', lazy='dynamic')
	works = db.relationship('Work', backref='work', lazy='dynamic')

