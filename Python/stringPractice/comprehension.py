import time
'''
start = time.time() #time1
L = range(1000000)
for x in xrange(len(L)):
    L[x] += 10
print(L, time.time() - start)
'''
'''
start = time.time() #time2
L = range(1000000)
L = [x + 10 for x in L]
print(L, time.time() - start)
'''

time1 = .2957489490509033
time2 = .27013397216796875

print time1 / time2 # List compre in this case is roughly 2x with lower ranges