import csv, sys
from math import sqrt

def prime():
	# https://en.wikibooks.org/wiki/Some_Basic_and_Inefficient_Prime_Number_Generating_Algorithms
	lim = input("\nGenerate prime numbers up to what number? : ")
	sqrtlim = sqrt(float(lim))
	ss=[2]
	ep=[2]
	rss=[2, 6]
	tp=[3, 5]
	pp = 3
	i=0
	pp = 5
	npp = 5
	while npp<int(lim):
		i+=1
		while npp<rss[i]+1:
			for n in ss:
				npp = pp + n
				if npp>int(lim): break
				if npp<=rss[i]+1: pp=npp
				sqrtnpp=sqrt(npp)
				test=True
				for q in tp:
					if sqrtnpp<q:
						break
					elif npp%q==0:
						test=False
						break
				if test:
					if npp<=sqrtlim:
						tp.append(npp)
			if npp>int(lim):
				break
		if npp>int(lim):
			break
		lrpp=pp
		nss=[]
		while pp < (rss[i]+1)*2-1:
			for n in ss:
				npp = pp + n
				if npp>int(lim):
					break
				sqrtnpp = sqrt(npp)
				test=True
				if sqrtnpp<q:
					break
				elif npp % q == 0:
					test = False
					break
				if test:
					if npp<=sqrtlim:
						tp.append(npp)
				if npp%tp[0]!=0:
					nss.append(npp-lrpp)
					lrpp=npp
				pp=npp
			if npp>int(lim):
				break
		if npp>int(lim):break
		ss=nss
		ep.append(tp[0])
		del tp[0]
		rss.append(rss[i]*tp[0])
		npp=lrpp
	ep.reverse()
	[tp.insert(0,a) for a in ep]
	tp.reverse()
	return tp