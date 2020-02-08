def count_vowels(input_string):
	"""Count the number of vowels in input_string"""

	vowels = 'aeiou'
	counter = 0
	for vowel in vowels:
		counter += input_string.count(vowel)

	return counter

# Testing
print(count_vowels('programmer')) # 3
print(count_vowels('hmm..')) # 0
