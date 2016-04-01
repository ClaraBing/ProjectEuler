# Pentagon numbers

# The function does not terminate.
def f():
	curr = 1
	persis = []
	while True:
		table = [i*(3*i-1)//2 for i in range(curr, curr+50)]
		persis.extend(table)
		s = set(persis)
		for i in range(49):
			for j in range(curr):
				pi = (table[i] - persis[j]) // 2
				pj = table[i] - pi
				if pi in s and pj in s:
					# the answer is the first number (persis[j]) I got
					# though don't know whether the first number is guaranteed to be the smallest
					print(str(pi)+" and "+str(pj)+" with difference = "+str(persis[j]))
		curr += 50

# table = [1, 5, 12, 22, 35, 51, 70, 92, 117, 145, 176, 210, 247, 287, 330, 376, 425, 477, 532, 590, 651, 715, 782, 852, 925, 1001, 1080, 1162, 1247, 1335, 1426, 1520, 1617, 1717, 1820, 1926, 2035, 2147, 2262, 2380, 2501, 2625, 2752, 2882, 3015, 3151, 3290, 3432, 3577]
# table = [1, 5, 12, 22, 35, 51, 70, 92, 117, 145, 176, 210, 247, 287, 330, 376, 425, 477,
#  532, 590, 651, 715, 782, 852, 925, 1001, 1080, 1162, 1247, 1335, 1426, 1520, 1617, 1717, 1820, 1926, 2035, 2147, 2262, 2380, 2501, 2625, 2752, 2882, 3015, 3151
# , 3290, 3432, 3577, 3725, 3876, 4030, 4187, 4347, 4510, 4676, 4845, 5017, 5192,
# 5370, 5551, 5735, 5922, 6112, 6305, 6501, 6700, 6902, 7107, 7315, 7526, 7740, 7957, 8177, 8400, 8626, 8855, 9087, 9322, 9560, 9801, 10045, 10292, 10542, 10795,
# 11051, 11310, 11572, 11837, 12105, 12376, 12650, 12927, 13207, 13490, 13776, 14065, 14357, 14652]


# generate pentagon numbers
def pen():
	return [i*(3*i-1)//2 for i in range(1, 100)]