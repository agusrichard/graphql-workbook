from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from ..models import Work, Category


class AddForm(FlaskForm):
	name = StringField('Name', placeholder='Name')
	work = SelectField('Work', placeholder='Work', coerce=int)
	salary = SelectField('Salary', placeholder='Work', coerce=int)

	def __init__(self, *args, **kwargs):
		super(AddForm, self).__init__(*args, **kwargs)
		self.work.choice = [(work.id, work.name) for work in Work.query.order_by(Work.name).all()]
		self.salary.choice = [(salary.id, salary.name) for salary in Category.query.order_by(Category.name).all()]

class EditForm(FlaskForm):
	name = StringField('Name', placeholder='Name')
	work = SelectField('Work', placeholder='Work', coerce=int)
	Salary = SelectField('Salary', placeholder='Work', coerce=int)

	def __init__(self, *args, **kwargs):
		super(AddForm, self).__init__(*args, **kwargs)
		self.work.choice = [(work.id, work.name) for work in Work.query.order_by(Work.name).all()]
		self.salary.choice = [(salary.id, salary.name) for salary in Category.query.order_by(Category.name).all()]
