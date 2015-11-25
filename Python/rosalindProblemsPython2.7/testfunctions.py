import dna_functions
dna = 'ATTTGGGGCCCC'

print('DNA strand entered: \t' + dna)
print('Reverse Compliment DNA: \t' + dna_functions.dna_reverse_compliment(dna))
print('DNA to RNA: \t' + dna_functions.dna_to_rna(dna))
print('DNA reverse compliment to RNA: \t' + dna_functions.dna_to_rna(dna_functions.dna_reverse_compliment(dna)))
print('RNA to protein: \t' + dna_functions.rna_to_protein(dna_functions.dna_to_rna(dna)))
print('Reverse RNA to Protein: \t' + dna_functions.rna_to_protein(dna_functions.dna_reverse_compliment(dna)))