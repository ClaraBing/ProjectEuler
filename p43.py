# Sub-string divisibility

from itertools import permutations

def f():
	d = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
	p = [2, 3, 5, 7, 11, 13, 17]
	res = []
	for num in permutations(d, 10):
		met = True
		for i in range(1, 8):
			if int(''.join([num[i], num[i+1], num[i+2]])) % p[i-1] != 0:
				met = False
				break
		if met:
			res.append(int(''.join(num)))
	return sum(res)