# Coded triangle numbers

# comma seperated value
import csv

def f():
	f = open('p042_words.csv')
	cnt = 1
	for row in csv.reader(f):
		# there is only 1 line in the file; not clear about the default delimiter of csv.reader
		return len([word for word in row if sum([ord(d)-64 for d in word]) in table])

# triangular number table
table = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190,
210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630,
666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225]

# function to generate triangular numbers
# only up to 1225 since the words in the file have length < 20, with each letter's value <= 26
def tri():
	t = []
	for i in range(1, 50):
		t.append(i*(i+1)//2)
	return t