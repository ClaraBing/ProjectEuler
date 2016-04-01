# product of ith digit

def f():
	cnt, i = 0, 1
	check, p = [1, 10, 100, 1000, 10000, 100000, 1000000], 0
	while cnt <= 1000010 and p<7:
		cnt += len(str(i))
		if cnt > check[p]:
			print("val: "+str(i)+"  cnt: "+str(cnt))
			p += 1
		i += 1