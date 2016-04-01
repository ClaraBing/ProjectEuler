# Amicable Numbers

def c():
	t = {}
	for i in range(1, 10000):
		t[i] = sof(i)
	ret = 0
	for i in range(1, 10000):
		if t[i]<10000 and i == t[t[i]] and i != t[i]:
			ret += i + t[i]
			print("a: "+str(i) + " / b: "+str(t[i]))
	return ret // 2 # since each pair is counted twice

# sum of proper factors
def sof(n):
	ret = 1
	for i in range(2, n):
		if n % i == 0:
			ret += i
	return ret