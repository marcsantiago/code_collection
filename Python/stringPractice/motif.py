with open('m.txt') as input_data:
    dna, k = [line.strip() for line in input_data.readlines()]
    k = int(k)

kmer_dict = dict()

for i in xrange(len(dna) - k + 1):
    if dna[i:i + k] in kmer_dict:
        kmer_dict[dna[i:i + k]] += 1
    else:
        kmer_dict[dna[i:i + k]] = 1

kmers = [item[0] for item in kmer_dict.items() if item[1] == max(kmer_dict.values())]

print ' '.join(kmers)
with open('Textbook_01A.txt', 'w') as output_data:
    output_data.write(' '.join(kmers))