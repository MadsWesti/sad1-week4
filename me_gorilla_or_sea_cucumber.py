import sys

def load_matrix():
	file = open('data/BLOSUM62.txt')
	data = file.readlines()[6:]
	file.close()
	data = [d.strip() for d in data]

	alphabet = data[0].split()
	data = data[1:]

	lookup = {}
	for index, a in enumerate(alphabet):
		lookup[a] = index

	#print lookup['*'],lookup['A']

	matrix = [[0 for i in range(0,23)] for j in range(0,23)]
	
	for k in matrix:
		for l in k:
			print l

	# for i,d in enumerate(data):
	# 	matrix[i] = d.split()[1:]
				
	# print matrix[0][0]		

	# values = data[1:]
	# for v in values:
	# 	for h in v.split():
	# 		print h

	


def parse_data():
	data = sys.stdin.read()
	return data

load_matrix()