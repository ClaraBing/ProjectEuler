# Counting Sundays

mdays = {0:31, 1:28, 2:31, 3:30, 4:31, 5:30, 6:31, 7:31, 8:30, 9:31, 10:30, 11:31}

def c():
	week = 1
	cnt = 0
	for i in range(1, 101):
		mdays[1] = 29 if (1900+i) % 4 == 0 else 28 # leap year
		for each in mdays:
			week = (week + mdays[each]) % 7
			if week == 6:
				cnt += 1
				print("Year "+str(1900+i)+" Month "+str(each+1))
	return cnt