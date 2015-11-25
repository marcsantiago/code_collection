def validate_base_sequence(base_sequence):
    seq = base_sequence.upper()
    return len(seq) == seq.count('A') + seq.count('G') + seq.count('T') + seq.count('C')


def dna_reverse_compliment(base_seq):
    """Takes a DNA sequence, reverses it ::-1
     and complements the nucleotide. E.g A<->T, G<->C"""
    assert validate_base_sequence(base_seq), \
        "Argument has invalid characters can only use A, T, G , C"
    dnastring = base_seq.upper()
    reverse_dna = dnastring[::-1]
    dna_complement_dict = {
        'A': 'T',
        'T': 'A',
        'G': 'C'
    }

string = 'aattggcc'
print dna_reverse_compliment(string)