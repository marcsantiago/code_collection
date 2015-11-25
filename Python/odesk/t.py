def split_by_n(seq, n):
    while seq:
        yield seq[:n]
        seq = seq[n:]

stop = True
while stop:
    number = input()
    if number == 0:
        break
    string = raw_input()

    gen = split_by_n(string, number)
    count = 1
    l = []
    for i in gen:
        if not count % 2 == 0:
            l.append(i)
            count += 1
        else:
            l.append(i[::-1])
            count += 1

    listtwo = []
    columnlength = len(string) / number
    count = 0
    while len(listtwo) != len(string):
        for i in xrange(len(l)):
            for j in xrange(columnlength):
                listtwo.append(l[i][count])
                break
        count += 1

    print ''.join(listtwo)
