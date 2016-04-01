def f():
	for i in range(500):
		for j in range(i):
			t = 1000*(i+j) - i*j
			if t == 500000:
				print("i: "+str(i)+";   j: "+str(j))
				return