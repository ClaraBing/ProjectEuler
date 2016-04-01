# Digit cancelling fractions

from operator import mul
from functools import reduce

def f():
	nums, dems = [], []
	# case 1: ka/bk
	for k in range(1, 10):
		for b in range(k, 10):
			for a in range(1, 10):
				if (10*b - a)*k == 9*a*b and k != a:
					print("case1: a: "+str(a)+";  b: "+str(b)+";  k: "+str(k))
					nums.append(a)
					dems.append(b)
	# case 2: ak/kb
	for k in range(1, 10):
		for a in range(1, k+1):
			for b in range(1, 10):
				if (10*a - b)*k == 9*a*b and k != a:
					print("case2: a: "+str(a)+";  b: "+str(b)+";  k: "+str(k))
					nums.append(a)
					dems.append(b)
	# relatively prime
	num = reduce(mul, nums)
	dem = reduce(mul, dems)
	for each in getPFact(num):
		if dem % each == 0:
			dem //= each
	return dem

# get prime factors
def getPFact(n):
	curr, plst = 2, [2]
	pfactors = []
	while n % curr == 0:
		n //= curr
		pfactors.append(curr)
	curr = 3
	plst = [2, 3]
	while n != 1:
		while n % curr == 0:
			n //= curr
			print(str(curr)+" ", end='')
			pfactors.append(curr)
		# get next prime
		while True:
			curr += 2
			found = False
			for p in plst:
				if curr % p == 0:
					found = False
					break
			if found:
				plst.append(curr)
				break
	return pfactors