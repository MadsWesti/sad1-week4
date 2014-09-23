import sys, itertools

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
    data = sys.stdin.read().splitlines()
    
    sequences = []
    #sequences = {}
    sequence = ""
    name = ""
    first_sequence = True
    for d in data:
        if d[0] == '>':
            if not first_sequence:
                sequences.append((name,sequence))
                #sequences[name] = sequence
            first_sequence = False
            name = d.split()[0][1:]
            sequence = ""
        else:
            sequence += d
    sequences.append((name,sequence))
    #sequences[name] = sequence
    for s in sequences:
        print s[1]
    return sequences

load_matrix()
data = parse_data()
a = "MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH"
b = "MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFKLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH"

#print alignment(a,b)
#loop through possible combinations of sequences - disregarding ordering
for sequence_1,sequence_2 in itertools.combinations(data, 2):
    alignment_solution = alignment(sequence_1[1],sequence_2[1])
    print sequence_1[0]+"--"+sequence_2[0]+": "+str(alignment_solution[2])
    print alignment_solution[0]
    print alignment_solution[1]
    