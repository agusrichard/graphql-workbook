import re

def is_username_valid(username):
	return re.match(r"^[a-z]{5,9}$", username) is not None

def is_password_valid(password):
	return re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})", password) is not None