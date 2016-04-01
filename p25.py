# the index of the first Fib number to have 1000 digits
def f():
	a = 1
	b = 1
	c = a+b
	cnt = 3
	while len(str(c)) < 1000:
		a = b
		b = c
		c = a+b
		cnt += 1
	print(cnt)