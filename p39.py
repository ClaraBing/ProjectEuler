# perimiter of right triangle: p<= 1000 with max number of triangles

import operator

def f():
	table = {}
	for s in range(10, 1001):
		table[s] = 0
		for a in range(s//3, s//2):
			for b in range(1, min(s-a, a)):
				c = s - a - b
				if a**2 == b**2 + c**2:
					table[s] += 1
	curr = 10
	for key in table:
		if table[key] > table[curr]:
			curr = key
	print(str(curr)+" with count = "+str(table[curr]))
	return curr