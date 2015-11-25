import dna_functions

data = open("rna_splicing.txt", "r").read().split(">")
del data[0]


dna = "".join(data[0].splitlines()[1:])

introns = []
for i in range(1, len(data)):
    introns.append("".join(data[i].splitlines()[1:]))


for i in range(len(introns)):
    dna = dna.replace(introns[i], "")

rna = dna_functions.convert_dna_to_rna(dna)
protein = dna_functions.rna_to_protein(rna)

print(protein)

