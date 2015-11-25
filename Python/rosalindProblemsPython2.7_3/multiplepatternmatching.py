with open('mulpattern.txt') as f:
    target = f.readline()[:]
    patterns = f.read().split()[:]

hits = []
for match in patterns:
    count = target.find(match)
    while count > -1:
        hits.append(count)
        count += 1
        count = target.find(match, count)
hits.sort()
print str(hits).replace(',', '')[1:-1]



