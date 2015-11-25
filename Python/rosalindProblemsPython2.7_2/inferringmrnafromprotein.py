protein_codon_count = {
    'G': 4,
    'A': 4,
    'V': 4,
    'L': 6,
    'I': 3,
    'P': 4,
    'F': 2,
    'Y': 2,
    'W': 1,
    'S': 6,
    'T': 4,
    'C': 2,
    'M': 1,
    'N': 2,
    'Q': 2,
    'K': 2,
    'R': 6,
    'H': 2,
    'D': 2,
    'E': 2,
    'B': 4,
    'Z': 4
}

string = open('rosalind_protein_string.txt', 'r').read().rstrip()

stopcodon = 3
count = 1
for letter in string:
        temp = protein_codon_count[letter]
        count *= int(temp)
print (count * stopcodon) % 1000000


