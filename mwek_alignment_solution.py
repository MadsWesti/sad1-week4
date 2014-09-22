import sys

M = {}
score_matrix = {}

def load_matrix():
    file_path = 'BLOSUM62.txt'
    file = open(file_path)
    data = file.readlines()[6:]
    file.close()
    data = [d.strip() for d in data]

    alphabet = data[0].split()
    data = data[1:]

    for i, a in enumerate(alphabet):
        for values in data:
            listed_values = values.split()
            score_matrix[a, listed_values[0]] = int(listed_values[i+1])

def alignment(X, Y):
    i = len(X)
    j = len(Y)

    if (i,j) in M:
        return M[i,j]

    delta = score_matrix['A','*']

    if i == 0:
        return '-'*j, Y, delta*j
    if j == 0:
        return X, '-'*i, delta*i

    X_i = X[-1]
    Y_j = Y[-1]
    
    match_score = score_matrix[X_i, Y_j]

    recursive_call1 = alignment(X[:-1], Y[:-1])
    result1 = recursive_call1[0] + X_i, recursive_call1[1] + Y_j,  match_score + recursive_call1[2]
    
    recursive_call2 = alignment(X[:-1], Y)
    result2 = recursive_call2[0] + X_i, recursive_call2[1] + '-',  delta + recursive_call2[2]
    
    recursive_call3 = alignment(X, Y[:-1])
    result3 = recursive_call3[0] + '-', recursive_call3[1] + Y_j,  delta + recursive_call3[2]

    max_result = get_max_tuple([result1, result2, result3])

    M[i,j] = max_result

    return max_result


def get_max_tuple(A):
    max_value = max(x[2] for x in A)    
    return [x for x in A if x[2] == max_value][0]

def parse_data():
    pass
    #parse stuff

load_matrix()
parse_data()

#hardcoded data
a = "KQRK"
b = "KAK"
c = "KQRIKAAKABK"
d = "MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH"
e = "VHLTPVEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH"

#print out
result = alignment(d,e)
print str(result[2])
print result[0]
print result[1]