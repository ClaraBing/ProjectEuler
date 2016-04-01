with open('p13.txt') as f:
	s = 0
	for x in f:
		print(x)
		s += int(x)
	print(s // 10000000000000000000000000000000000000000)