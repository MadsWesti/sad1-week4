import sys


def load_matrix():
    file = open('data/BLOSUM62.txt')
    data = file.readlines()[6:]
    file.close()
    data = [d.strip() for d in data]

    alphabet = data[0].split()
    data = data[1:]

    matrix = {}
    for i, a in enumerate(alphabet):
        for values in data:
            listed_values = values.split()
            matrix[a, listed_values[0]] = listed_values[i+1]
    

def parse_data():
    data = sys.stdin.read().splitlines()
    data = [d.strip() for d in data]
    proteinmatrix = {}
    species = ""
    for line in data:
        #print line
        if line[0] == ">":
            if species != "":
                proteinmatrix[species] =  proteinseq
            proteinseq = ""
            species = line.strip()[1:]
        else:
            proteinseq = proteinseq + line.strip()
    
    print proteinmatrix["Sphinx"]


load_matrix()
parse_data()
