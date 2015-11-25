def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)  #recursive call to function

for i in xrange(0, input()):
    a, b = raw_input().split()
    a = int(a)
    b = int(b)
    print gcd(a, b)
