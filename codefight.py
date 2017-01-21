def check(n, arr):
  num = 0
  arr = [float(s) for s in arr]

  for i in arr:
    num += i

  if str(num) == str(n):
    return True
  else:
    return False

n = "7970521.5544"
parts = n.split(".")

matrix = []
count = 1
for i in xrange(len(parts[0])):
  if parts[0][i] != '0':
    matrix.append(parts[0][i] + '0' * (len(parts[0]) - count))
  count += 1

count = 0
for i in xrange(len(parts[1])):
  if parts[1][i] != '0':
    matrix.append(('.' + '0' * count) + parts[1][i] )
  count += 1

print matrix
print check(n, matrix)
