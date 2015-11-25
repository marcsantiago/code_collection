string = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
a = 0
g = 0
c = 0
t = 0
for letter in string:
    if letter == 'A':
        a += 1
    elif letter == 'G':
        g += 1
    elif letter == 'C':
        c += 1
    elif letter == 'T':
        t += 1
print(a, c, g, t)
