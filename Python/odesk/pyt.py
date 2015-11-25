__author__ = 'marc santago'
#!/usr/bin/python2.7
_author_ = 'Marc Santiago'
import math

q = True
while q:
    print('\n')
    print('Unknown Pythagorean Solver a^2 + b^2 = c^2')
    print('If variable is unknown enter x')
    a = raw_input('Enter a\t')
    b = raw_input('Enter b\t')
    c = raw_input('Enter c\t')

    if a.lower() == 'x':
        solution = math.sqrt((int(c) ** 2) - (int(b) ** 2))
        print('A: ' + str(solution))

    if b.lower() == 'x':
        solution = math.sqrt((int(c) ** 2) - (int(a) ** 2))
        print('B: ' + str(solution))

    if c.lower() == 'x':
        solution = math.sqrt((int(a) ** 2) + (int(b) ** 2))
        print('C: ' + str(solution))
    if a.lower() != 'x' and b.lower() != 'x' and c.lower() != 'x':
        print('Error, all variables are known')

    test = raw_input('Run another test: yes or no\n')
    if test == 'no':
        q = False