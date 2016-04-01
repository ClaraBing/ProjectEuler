# Pandigital multiples

from itertools import permutations

d = {1,2,3,4,5,6,7,8,9}

def f():
	for num in permutations(d, 4):
		#print(num)
		if num[0]<5:
			continue
		if {int(x) for x in str(2 * (num[0]*1000+num[1]*100+num[2]*10+num[3]))}.union(set(num)) == d:
			print(num)