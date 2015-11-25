from math import factorial
'''
string = 'CUAUUUCAGCGUGCCCUAUAUCCAAUGUUCGGUGCCAAGAGUUCGAGCGUAAUGCAGUACAGUUGACACAAAUG'
print math.factorial(string.count('A')) * math.factorial(string.count('G'))

'''

string = 'AGCAGCAUCGCACAUGGAGCUCGGAAAAAAUGUGAAGUUAUUAGAUCUGUGAGGUGCUGUGUUAUACGCGGACCCGUCGUAGAUACCC'
def problem(rna):
    a, u, g, c = map(rna.count, ["A", "U", "G", "C"])
    a = factorial(max(a, u)) / factorial(max(a, u) - min(a, u))
    b = factorial(max(g, c)) / factorial(max(g, c) - min(g, c))
    return a * b


print problem(string)