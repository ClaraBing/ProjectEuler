# this file contains all the possible functions related to primes

# read plst from prime table (txt)
def readp():
	fin = open('primes1.txt', 'r')
	bound = 19650
	plst = [int(p) for cnt,line in enumerate(fin) for p in line.split() if cnt<bound]
	fout = open('ptable.txt', 'w')
	fout.write(str(plst))