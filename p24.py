import math

def p():
	#curr = 1000000
	curr = 999999
	lst = [0,1,2,3,4,5,6,7,8,9]
	for i in range(9, -1, -1):
		idx = curr // math.factorial(i)
		curr %= math.factorial(i)
		print(lst[idx], end='')
		lst.pop(idx)
	print()