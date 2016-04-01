# Find a*b (|a|, |b|<1000) such that n^2 + an + b produces the longest prime seqeunce

gp = set([2])

# bound: only generate primes less than bound;
# if overflow is reported during the computation in f(), raise the bound
# (maybe use prime test instead)
def gen():
	bound = 100000
	largest = 2
	for i in range(3, bound, 2):
		found = True
		for p in gp:
			if i % p == 0:
				found = False
				break
		if found:
			gp.add(i)
			largest = i
	return largest

# a: odd; b: prime
def f():
	pair = {} # (key, val) = (length, (a,b))
	largest = gen()
	primes = [2] # a list of primes less than 1000
	for i in range(3, 1000, 2):
		found = True
		for p in primes:
			if i % p == 0:
				found = False
				break
		if found:
			primes.append(i)
	for p in primes: # b
		for i in range(1, 1000, 2): # a
			pos, res = 0, p
			while res in gp:
				pos += 1
				res = pos*pos + i*pos + p
				if res > largest:
					print("overflow: "+str(res))
					print("pos length: "+str(pos))
					return
			neg, res = 0, p
			while res in gp:
				neg += 1
				res = neg*neg - i*neg + p
				if res > largest:
					print("overflow: "+str(res))
					print("neg length: "+str(neg))
					return
			if pos < neg:
				pair[neg] = (-i, p)
			else:
				pair[pos] = (i, p)
	print("winning pair: a="+str(pair[max(pair)][0])+", b="+str(pair[max(pair)][1]))
	return pair[max(pair)][0] * pair[max(pair)][1]