from math import sqrt, ceil
from operator import mul
from functools import reduce
from datetime import datetime

def countFactor(n):
	cnt = 0
	for i in range(1, ceil(sqrt(n))):
		if n % i == 0:
			cnt += 2
	if sqrt(n) * sqrt(n) == n:
		cnt -= 1
	return cnt

# find and count the prime factors
def pf(n):
	pl = [2] # prime number list
	p = 2
	fl = {} # prime factor dict
	while n != 1:
		fl[p] = 0
		while n % p == 0:
			n //= p
			fl[p] += 1
		# curr = p+1 if p == 2 else curr = p+2
		found = False
		while not found:
			p = p+1 if p == 2 else p+2
			found = True
			for each in pl:
				if p % each == 0:
					found = False
					break
		pl.append(p)
	return reduce(mul, [fl[k] + 1 if fl[k] > 1 else 2 ** fl[k] for k in fl], 1)


def find():
	tri, i = 125*251, 251
	cnt = 0
	start = datetime.now()
	while countFactor(tri) < 500:
		tri += i
		i += 1
	end = datetime.now()
	delta = start - end
	print("BF: "+ str(delta.microseconds))
	start = datetime.now()
	tri, i = 125*251, 251
	cnt = 0
	while pf(tri) < 500:
		tri += i
		i += 1
	end = datetime.now()
	print("PF: "+ str(delta.microseconds))
	return tri