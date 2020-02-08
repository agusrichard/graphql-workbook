def count_vowels(input_string):
	"""Count the number of vowels in input_string"""

	vowels = 'aeiou'
	counter = 0
	for vowel in vowels:
		counter += input_string.count(vowel)
	return counter
