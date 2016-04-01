# Digit factorials

table = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720, 7:5040, 8:40320, 9:362880}

# 2-7 digits
def f():
	lst = [i for i in range(10, 2540160) if sum([table[int(digit)] for digit in str(i)]) == i]
	print("sum of "+str(lst)+": ", end='')
	return sum(lst)
