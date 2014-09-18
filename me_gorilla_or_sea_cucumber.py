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


def parse_data():
    data = sys.stdin.read()
    return data

load_matrix()
