# Find the number of distinct values generated by a^b

def n(a, b):
	res = set([])
	for base in range(2, a+1):
		for power in range(2, b+1):
			res.add(base ** power)
	return len(res)