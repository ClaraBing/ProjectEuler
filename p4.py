ret = 0
for i in range(999):
	for j in range(999):
		mul = i*j
		if str(mul) == str(mul)[::-1]:
			ret = max(ret, mul)
print(ret)