s = 0
for i in range(2, 101):
	for j in range(1, i):
		s += i*j
print(s)