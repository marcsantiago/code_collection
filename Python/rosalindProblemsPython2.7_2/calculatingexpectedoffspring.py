probs = [2., 2., 2., 1.5, 1, 0]

with open('rosalind_iev.txt', 'r') as f:
    couples = map(int, f.readline().split())

print sum([a * b for a, b in zip(probs, couples)])

