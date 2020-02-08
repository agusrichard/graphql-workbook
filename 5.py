def fibonacci_sequence(n_elements):
	"""Return fibonacci sequence as a list"""

	fibo_seq = [0, 1]
	while len(fibo_seq) < n_elements:
		fibo_seq.append(fibo_seq[-2]+fibo_seq[-1])

	return fibo_seq


def fibo(cols, rows):
	"""Print fibonacci sequence in a row-column format"""

	fibo_seq = fibonacci_sequence(cols*rows)
	for i in range(rows):
		output_str = ""
		for j in range(cols*i, cols*i+cols):
			output_str += (str(fibo_seq[j]) + ', ')
		print(output_str)

# Testing
fibo(4, 3) 
