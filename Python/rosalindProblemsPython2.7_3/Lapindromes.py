t = input()
l = []

for i in xrange(0, int(t)):
        l.append(raw_input())

for x in l:
    if len(x) % 2 == 0:
        firsth = x[:len(x) / 2]
        secondh = x[len(x) / 2:]

        if sorted(firsth) == sorted(secondh):
            print 'YES'
        else:
            print 'NO'

    elif len(x) % 2 != 0:
        firsth = x[:len(x) / 2]
        secondh = x[len(x) / 2 + 1:]

        if sorted(firsth) == sorted(secondh):
            print 'YES'
        else:
            print 'NO'

