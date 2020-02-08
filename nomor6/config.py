import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or "ea75882e2040f75b6dc7a1b55e3ba5af1b6c19561288fb36402510d3fcce6c2b"
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'data.sqlite')
	SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
	'default': Config
}