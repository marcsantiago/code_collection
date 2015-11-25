import math
size, partial = file('P_Permutations.txt', 'r').read().split()
n = int(size)
k = int(partial)

print n, k

answer = math.factorial(n) / math.factorial((n - k))
'''Partial factorial is equal to
p = (n!) / ((n-k)!)'''

print answer % 1000000