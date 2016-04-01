# coins
cs = [1, 2, 5, 10, 20, 50, 100, 200]

def c(t, lst):
	if t == 0:
		return 1
	if lst == [] or t < lst[0]:
		return 0
	return c(t-lst[0], lst) + c(t, lst[1:])