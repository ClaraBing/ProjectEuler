# the sum of name scores

def get():
	lst = [name for line in open("p22.txt") for name in line.split("\",\"")]
	lst[0] = lst[0][1:]
	lst[-1] = lst[-1][:-1]
	return sum([(pos+1) * sum([ord(char) - 64 for char in word]) for pos, word in enumerate(mergeSort(lst))])

def mergeSort(lst):
	if len(lst) <= 1:
		return lst
	s1, s2 = mergeSort(lst[:len(lst)//2]), mergeSort(lst[len(lst)//2:])
	# merge
	merged = []
	while s1 != [] and s2 != []:
		if s1[0] <= s2[0]:
			merged.append(s1[0])
			s1 = s1[1:]
		else:
			merged.append(s2[0])
			s2 = s2[1:]
	return merged + (s2 if s1 == [] else s1)