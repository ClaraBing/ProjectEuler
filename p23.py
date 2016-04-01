# find all abundant numbers -> get their sum -> subtract from the Gaussian total
def nas():
	abundant = [n for n in range(1, 28124) if sum([i for i in range(1, n) if n % i == 0]) > n]
	return (1+28123)*28123//2 - sum(set([abundant[i] + abundant[j] for i in range(len(abundant)) for j in range(i+1) if abundant[i] + abundant[j] < 28124]))