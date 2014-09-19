import sys


matrix = {}


def load_matrix():
    file = open('data/BLOSUM62.txt')
    data = file.readlines()[6:]
    file.close()
    data = [d.strip() for d in data]

    alphabet = data[0].split()
    data = data[1:]

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
        if line[0] == ">": 
            if species != "":
                proteinmatrix[species] =  proteinseq
            proteinseq = ""
            species = line.strip()[1:].split()[0]
        else:
            proteinseq = proteinseq + line.strip()
    proteinmatrix[species] = proteinseq # puts in the last species. Could prettify if we want.

    for name1 in proteinmatrix:
        for name2 in proteinmatrix:
            if name1 == name2:
                continue
            else:
                seq1 = proteinmatrix[name1]
                seq2 = proteinmatrix[name2]
                
                cheapest = find_sum(seq1, seq2, 0)

                #print name1 + " and " + name2 + " has score: " + str(cheapest)
                print cheapest
    
def find_sum(s1, s2, sum):


    # the last chars in the strings
    chr1 = s1[-1]
    chr2 = s2[-1]

    # the new strings, one char shorter
    s1 = s1[:len(s1)-1]
    s2 = s2[:len(s2)-1]

    # the max length of the strings
    i = max(len(s1), len(s2))

    # Both of the strings, concatenated with a dash
    dash1 = insert_dash(s1)
    dash2 = insert_dash(s2)

    sum = sum + int(matrix[chr1, chr2])

    print s1 + " " + s2 + " " + dash1 + " " + dash2 + " " + chr1 + chr2 + str(sum)

    if len(s1) == 0:
        return sum
    else:
        find_sum(s1, s2, sum)
    

    #while i > 1:
        #sum = max(find_sum(dash1,s2,sum),find_sum(s1,dash2,sum),find_sum(s1,s2,sum))
    #else: 
        #return sum

    #while i > 0:
        #alpha = s1[i]
        #beta = s2[i]
        #sum = sum + int(matrix[alpha, beta])
        #i = i-1


def compare_sums(sum1, sum2):
    if sum1 < sum2:
        return sum2
    else:
        return sum1


def insert_dash(string):
    return string + "-"


load_matrix()
parse_data()
