# Find the longest reciprocal cycles

def l():
	cover = [0, 10, 100, 1000]
	final = {} # (key ,val) = length, d
	for k in range(len(cover)-1):
		for i in range(cover[k]+1, cover[k+1]):
			appeared = {}
			r = 1
			pos = 0
			while r != 0 and r not in appeared:
				appeared[r] = pos
				r = (r * cover[k+1]) % i
				pos += 1
			if r != 0:
				final[pos - appeared[r]] = i
	return final[max(final)]