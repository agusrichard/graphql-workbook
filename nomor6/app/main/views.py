from flask import render_template, redirect, url_for
from .  import main
from .forms import AddForm, EditForm
from ..models import Work, Category
from .. import db

@main.route('/')
def index():
	add_form = AddForm()
	edit_form = EditForm()
	if add_form.validate_on_submit():
		name = Name(name=add_form.name.data,
					id_work=Work.query.get(add_form.work.data),
					id_salary=Category.query.get(add_form.salary.data))
		db.session.add(name)
		db.session.commit()
		return redirect(url_for('main.index'))`		
	return render_template('base.html', add_form=add_form, edit_form=edit_form)