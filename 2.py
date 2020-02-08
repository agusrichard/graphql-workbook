import re

def is_username_valid(username):
	"""Return True if the username is valid based on predefined specification"""

	return re.match(r"^[a-z]{5,9}$", username) is not None

def is_password_valid(password):
	"""Return True if the password is valid based on predefined specification"""

	return re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})", password) is not None
	

# Testing
print(is_username_valid('cod3r')) # False
print(is_username_valid('siska')) # True
print(is_password_valid('cod3r')) # False
print(is_password_valid('codeYourFuture!123’')) # True
