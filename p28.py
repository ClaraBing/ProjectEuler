# Find the sum of the diagonal elements in a clockwise spiral

def s():
	bound = 1001*1001
	ret, curr, step = 1, 1, 2
	while curr < bound:
		ret += curr * 4 + step * 10
		curr += step * 4
		step += 2
	return ret