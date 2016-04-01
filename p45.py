# Triangular, pentagonal, and hexagonal

# This function does not terminate.
def f():
	bound, curr, i = 0, 1, 1
	while True:
		tri = i * (i+1)
		if tri > bound:
			table = [j*(3*j-1) for j in range(curr, curr+50)]
			curr += 50
			bound = (curr-1) * (3*curr - 4)
		if tri in table and i % 2 == 1:
			print(str(i) +": "+ str(tri//2))
		i += 1