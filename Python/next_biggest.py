import itertools

def next_bigger(n):
  copy = n
  n = list(str(n))

  combos = sorted(list(set(filter(lambda x: len(str(x)) == len(n) and x >= copy, [int("".join(i)) for i in list(itertools.permutations(n, len(n)))]))))
  print combos
  try:
    return combos[1]
  except IndexError:
    return -1

print next_bigger(414)
