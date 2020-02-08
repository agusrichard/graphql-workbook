from flask_wtf import FlaskForm
from wtforms import StringField, SelectField


class AddForm:
	name = StringField('Name', placeholder='Name')
	