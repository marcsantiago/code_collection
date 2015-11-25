data = open('trans_tran.txt', 'r').read().split('>')
del data[0]

# problem states that each string is the same length
firstsequence = ''.join(data[0].splitlines()[1:])
secondsequence = ''.join(data[1].splitlines()[1:])
stringlength = len(firstsequence)

transition = 0  # A<->G, C<->T

for i in xrange(0, stringlength):
    if firstsequence[i] is 'A' and secondsequence[i] is 'G':
        transition += 1
    if firstsequence[i] is 'G' and secondsequence[i] is 'A':
        transition += 1
    if firstsequence[i] is 'C' and secondsequence[i] is 'T':
        transition += 1
    if firstsequence[i] is 'T' and secondsequence[i] is 'C':
        transition += 1


transversion = 0  # A<->C, A<->T, G<->C, G<->T

for x in xrange(0, stringlength):
    if firstsequence[x] is 'A' and secondsequence[x] is 'C':
        transversion += 1
    if firstsequence[x] is 'C' and secondsequence[x] is 'A':
        transversion += 1
    if firstsequence[x] is 'A' and secondsequence[x] is 'T':
        transversion += 1
    if firstsequence[x] is 'T' and secondsequence[x] is 'A':
        transversion += 1
    if firstsequence[x] is 'G' and secondsequence[x] is 'C':
        transversion += 1
    if firstsequence[x] is 'C' and secondsequence[x] is 'G':
        transversion += 1
    if firstsequence[x] is 'G' and secondsequence[x] is 'T':
        transversion += 1
    if firstsequence[x] is 'T' and secondsequence[x] is 'G':
        transversion += 1


print("Number of transitions: " + str(transition))
print("Number of transversion: " + str(transversion))

ratio = (transition * 1.0 / transversion * 1.0)

print 'Ratio', "%0.11f" % ratio