d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# p:possible combinations:
# the key is the multiplicand and the elems in the list are the possible thousand digit of the multiplier
p = {2:[1,3,4], 3:[1,2], 4:[1,2]}

from itertools import combinations, permutations

def f():
	out = open("out.txt", 'w')
	ret = set([])
	# 1, 4, 4
	for a in p:
		for d1 in p[a]:
			tmp = [x for x in d if x != a and x != d1]
			for tri in permutations(tmp, 3):
				b = (d1*1000 + tri[0]*100 + tri[1]*10 + tri[2])
				prod = a * b
				res = set([int(char) for char in str(prod)]) # digits in the product
				tmp2 = {a, d1, tri[0], tri[1], tri[2]} # digits in the multiplicant + multiplier
				if 0 not in res and prod < 10000 and len(res) == 4 and len(res.intersection(tmp2)) == 0:
					ret.add(prod)
					out.write(str(a)+" * "+str(b)+" = "+str(prod)+"\n")
	# 2, 3, 4
	for a in permutations(d, 2):
		tmp = [x for x in d if x != a[0] and x != a[1]]
		for b in permutations(tmp, 3):
			fst, snd = a[0]*10 + a[1], b[0]*100 + b[1]*10 + b[2]
			prod = fst * snd
			res = set([int(char) for char in str(prod)]) # digits in the product
			tmp2 = {a[0], a[1], b[0], b[1], b[2]} # digits in the multiplicant + multiplier
			if 0 not in res and prod < 10000 and len(res) == 4 and len(res.intersection(tmp2)) == 0:
				ret.add(prod)
				out.write(str(fst)+" * "+str(snd)+" = "+str(prod)+"\n")
	return sum(ret)