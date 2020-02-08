import os
from app import create_app, db
from app.models import Name, Work, Category

app = create_app('default')

@app.shell_context_processor
def make_shell_context():
	return dict(db=db, Name=Name, Work=Work, Category=Category)


if __name__ == '__main__':
	app.run()