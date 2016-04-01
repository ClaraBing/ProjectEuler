# digit sum of 100!

def ps():
	p = 1
	for i in range(1, 101):
		p *= i
	s = 0
	while p > 0:
		s += p % 10
		p //= 10
	return s