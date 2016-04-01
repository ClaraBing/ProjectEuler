BOUND = 1000000

# a dictionary for DP
t = {1: 1}

def f():
	for i in range(1, 1000001):
		get(i)
	cnt = max(t.values())
	for k in t:
		if t[k] == cnt:
			return k

def get(i):
	if i in t:
		return t[i]
	if i % 2 == 0:
		t[i] = 1 + get(i // 2)
	else:
		t[i] = 1 + get(3*i + 1)
	return t[i]

# find the length of the longest Collatz sequence ending at n
# def cnt(n):
# 	if n in t:
# 		return t[n]
# 	if n > BOUND:
# 		if (n-1) % 3 == 0 and ((n-1) // 3) % 2 == 1:
# 			return 1 + cnt((n-1) // 3)
# 		return 0
# 	if (n-1) % 3 == 0 and ((n-1) // 3) % 2 == 1:
# 		t[n] = 1 + max(cnt((n-1) // 3), cnt(2*n))
# 		return t[n]
# 	t[n] = 1 + cnt(2*n)
# 	return t[n]