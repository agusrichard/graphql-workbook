def count_vowels(input_string):
	"""Return number of vowels in a string"""
	
	vowels = 'aeiou'
	counter = 0
	for vowel in vowels:
		counter += input_string.count(vowel)
	return counter
