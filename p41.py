# Pandigital prime

from itertools import permutations
from math import sqrt

def f():
	d = {'1','2','3','4','5','6','7'}
	end = {'2','4','6','8','5'}
	curr = 0
	for num in sorted(list(permutations(d, 7)))[::-1]:
		if num[-1] in end:
			continue
		if prime(int(''.join(num))):
			return int(''.join(num))

def prime(n):
	plst, curr = [2, 3], 3
	while curr < sqrt(n):
		if n % curr == 0:
			return False
		found = False
		while not found:
			curr += 2
			found = True
			for p in plst:
				if p < sqrt(curr) and curr % p == 0:
					found = False
					break
			if found:
				plst.append(curr)
				break
	return True