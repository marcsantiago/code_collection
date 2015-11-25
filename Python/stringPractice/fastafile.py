myFile = open('fasta.txt')
seq = []
for lines in myFile:
    if not lines.startswith('>'):
        seq.append(lines)
mySequences = "".join(seq)
del seq
myFile.close()

def common_motif_in_strings(strings):  #Can enter any number of strings
    strings = sorted(strings.split())
    short_string = strings[0]
    other_strings = strings[1:]

    l = len(short_string)
    m = ''
    for i in range(0, l):
        for j in range(l, i + len(m), -1):
            s1 = short_string[i:j]

            matched_all = True
            for s2 in other_strings:
                if s1 not in s2:
                    matched_all = False
                    break

            if matched_all:
                m = s1
                break

    return m

print(common_motif_in_strings(mySequences))




