# Maximum Path Sum I

def c(n):
	t = {}
	# read numbers from file and put them in iterator "lst" in the reverse order
	lst = iter([int(x) for line in open("p18.txt") for x in line.split()][::-1])
	for i in range(n, 0, -1):
		t[(n, i)] = next(lst)
	for i in range(n-1, 0, -1): # row
		for j in range(i, 0, -1): # col
			if (i, j) not in t:
				t[(i, j)] = next(lst) + max(t[(i+1, j)], t[(i+1, j+1)])
	return t[(1,1)]