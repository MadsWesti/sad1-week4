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
    
    for i in range(0,23):
        numberlist = data[i].split()
        for j in range(0,23):
            matrix[j][i] = numberlist[j+1]

    print matrix[0][0]
    print matrix[0][1]
    print matrix[0][2]
    print matrix[0][3]
    print matrix[0][4]
    print matrix[0][5]

    matrix2 = {}
    for i, a in enumerate(alphabet):
        for values in data:
            listed_values = values.split()
            matrix2[a, listed_values[0]] = listed_values[i+1]
    
    print "matrix2 AA", matrix2['A','A']
    print "matrix2 AR", matrix2['A','R']
    print "matrix2 AN", matrix2['A','N']
    print "matrix2 AD", matrix2['A','D']
    print "matrix2 AC", matrix2['A','C']
    print "matrix2 A*", matrix2['A','*']


def parse_data():
    data = sys.stdin.read()
    return data

load_matrix()
