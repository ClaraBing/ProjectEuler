# find the sum of all numbers that are palindrome in both base 10 and base 2

def s():
	t = 0
	for i in range(1, 1000000):
		b = str(bin(i))[2:]
		if str(i) == str(i)[::-1] and b == b[::-1]:
			t += i
	return t