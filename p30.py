# Find the sum of all number n s.t. n = ∑(i^5), where i is the digit of n

def f():
	# test up to 354294 = 6 * (9**5) since 7 * (9**5) < 1000000
	return sum([i for i in range(2, 354294+1) if i == sum([int(each) ** 5 for each in str(i)])])