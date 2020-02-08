from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from ..models import Work, Category


class AddForm(FlaskForm):
	name = StringField('Name', render_kw={"placeholder": "Name"})
	work = SelectField('Work', coerce=int, render_kw={"placeholder": "Work"})
	salary = SelectField('Salary', render_kw={"placeholder": "Salary"}, coerce=int)
	submit = SubmitField('Add')

	def __init__(self, *args, **kwargs):
		super(AddForm, self).__init__(*args, **kwargs)
		self.work.choice = [(work.id, work.name) for work in Work.query.order_by(Work.name).all()]
		self.salary.choice = [(salary.id, salary.name) for salary in Category.query.all()]

class EditForm(FlaskForm):
	name = StringField('Name', render_kw={"placeholder": "Name"})
	work = SelectField('Work', coerce=int, render_kw={"placeholder": "Work"})
	salary = SelectField('Salary', render_kw={"placeholder": "Salary"}, coerce=int)
	submit = SubmitField('Edit')

	def __init__(self, *args, **kwargs):
		super(EditForm, self).__init__(*args, **kwargs)
		self.work.choice = [(work.id, work.name) for work in Work.query.order_by(Work.name).all()]
		self.salary.choice = [(salary.id, salary.name) for salary in Category.query.all()]
