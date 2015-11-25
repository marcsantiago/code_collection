def longest_increasing_subsequence(d):
    '''Return one of the L.I.S. of list d'''
    l = []
    for i in range(len(d)):
        l.append(max([l[j] for j in range(i) if l[j][-1] < d[i]] or [[]], key=len)
                 + [d[i]])
    return max(l, key=len)


def longest_decreasing_subsequence(A):
    m = [0] * len(A)
    for x in range(len(A) - 2, -1, -1):
        for y in range(len(A) - 1, x, -1):
            if m[x] <= m[y] and A[x] > A[y]:
                m[x] = m[y] + 1
    max_value = max(m)

    result = []
    for i in range(len(m)):
        if max_value == m[i]:
            result.append(A[i])
            max_value -= 1

    return result

with open('seq.txt') as data:
    s = data.readlines()

sequence = []
for i in s:
    if i != ' ':
        sequence.append(i)

long = longest_increasing_subsequence(sequence)
short = longest_decreasing_subsequence(sequence)

print str(long).replace(',', '').replace("'", '')[1:-1]
print str(short).replace(',', '').replace("'", '')[1:-1]
