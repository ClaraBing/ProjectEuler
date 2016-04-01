from math import *

def lf(n):
	gen = prime([2])
	lim = sqrt(n)
	largest = 1
	for i in gen:
		while n % i == 0:
			largest = i
			print(i)
			n //= i
		lim = sqrt(n)
		if i>lim:
			if isPrime(n):
				print(n)
			else:
				print(largest)
			break
	return

def isPrime(n):
	ps = prime([2])
	lim = sqrt(n)
	for p in ps:
		if p > lim:
			return True
		if n % p == 0: 
			print("factor: "+str(p))
			return False

def prime(tested):
	#yield 2
	curr = 3
	s = 2
	while curr < 2000000:
		s += curr
		#yield curr
		curr += 2
		lim = sqrt(curr)
		new = True
		found = False
		while not found:
			found = True
			for i in tested:
				if curr % i == 0:
					curr += 2
					found = False
					break
		tested.append(curr)
	return s

# this function alone could work
def gl(n):
	orig = n
	p = 2
	f = 1
	tested = [2]
	while n % p == 0:
		n //= p
		f *= p
	p = 3
	while n != 1 and not (f >= 100 and f<1000 and orig//f >= 100 and orig//f < 1000):
		while n % p == 0:
			n //= p
			f *= p
			print(p)
		p += 2
		found = False
		while not found:
			found = True
			for i in tested:
				if p % i == 0:
					p += 2
					found = False
					break
		tested.append(p)
	# print("largest: "+str(tested[-2]))
	if n != 1:
		print("palindrome: "+str(orig))
		print("factor: "+str(f))
		return True
	else:
		return False

def pl():
	curr = 999999
	for i in range(9):
		t1 = curr
		for j in range(9):
			t2 = curr
			# if curr == 999999:
			# 	curr -= 10010
			# 	break
			for k in range(9):
				print(curr)
				if curr< 998001 and gl(curr):
					return
				else:
					curr -= 1100
			curr = t2 - 10010
		curr = t1 - 100001 


# lim = sqrt(n)
# 	largest = 1
# 	for i in gen:
# 		while n % i == 0:
# 			largest = i
# 			n //= i
# 		lim = sqrt(n)
# 		if i>lim:
# 			if isPrime(n):
# 				print(n)
# 			else:
# 				print(largest)
# 			break
# 	return



#
def p(lim):
	sqrtlim=sqrt(lim)
	pp=2
	ss = [pp]
	ep = [pp]
	pp += 1
	rss = [ss[0]]
	tp = [pp]
	xp = []
	i = 0
	rss.append(rss[i]*tp[0])
	pp += ss[0]
	npp = pp
	tp.append(npp)
	while npp < lim:
		i += 1
		while npp < rss[i]+1:
			for n in ss:
				npp = pp+n
				if npp > lim:
					break
				if npp<=rss[i]+1:
					pp = npp
				sqrtnpp = sqrt(npp)
				test = True
				for q in tp:
					if q > sqrtnpp:
						break
					if npp % q == 0:
						test = False
						break
				if test:
					if npp<=sqrtlim:
						tp.append(npp)
					else:
						xp.append(npp)
			if npp > lim:
				break
		if npp > lim:
			break
		lrpp = pp
		nss = []
		while pp < (rss[i]+1)*2-1:
			for n in ss:
				npp = pp+n
				if npp > lim:
					break
				sqrtnpp = sqrt(npp)
				test = True
				for q in tp:
					if q > sqrtnpp:
						break
					if npp % q == 0:
						test = False
						break
				if test:
					if npp <= sqrtlim:
						tp.append(npp)
					else:
						xp.append(npp)
				if npp%tp[0]!=0:
					nss.append(npp-lrpp)
					lrpp = npp
				pp = npp
			if npp > lim:
				break
		if npp > lim:
			break
		ss = nss
		ep.append(tp[0])
		del tp[0]
		rss.append(rss[i]*tp[0])
		npp = lrpp
	ep.reverse()
	[tp.insert(0,a) for a in ep]
	tp.reverse()
	[xp.insert(0,a) for a in tp]
	return xp