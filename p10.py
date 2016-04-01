# sum of primes below 2 million

def s():
	primes = [2, 3]
	ret = 0
	for i in range(5, 2000000, 2):
		p = True
		for x in primes:
			if i % x == 0:
				p = False
				break
		if p:
			primes.append(i)
			ret += i
			print(i)
	return ret