from math import sqrt

def check_triangle(values):
  if (values[0] + values[1] > values[2]) and (values[0] + values[2] > values[1]) and (values[1] + values[2] > values[0]):
    return True
  return False

values = []
# a and b are the two legs and c the hypotenuse
for c in ['a', 'b', 'c']:
  i = raw_input("Enter {0}: ".format(c))
  try:
    values.append(int(i))
  except ValueError:
    print 'All values entered must be integers'
    break

if check_triangle(values):
  # test to see if all the values in the list are the same
  if values[1:] == values[:-1]:
    print "Equilateral triangle."
  # if the len is not the same, then there was a dup, so it's iso
  elif len(values) != len(set(values)):
    print "Isosceles triangle."
  # check to see if its a right tri sqrt(a^2 + b^2) == c
  elif sqrt(((values[0] ** 2) + (values[1] ** 2))) == values[2]:
    print "Right triangle."
  else:
    print "Scalene Triangle."
else:
  print "this is not a triangle"