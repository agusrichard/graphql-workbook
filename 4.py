def ganti_kata(input_string, old_letter, new_letter):
	"""Return new string with old_letter replaced by new_letter"""

	for i in range(len(input_string)):
		if input_string[i] == old_letter:
			input_string = input_string[:i] + new_letter + input_string[i+1:]

	return input_string


# Testing
print(ganti_kata('Tuban', 'a', 'u')) # Tubun

