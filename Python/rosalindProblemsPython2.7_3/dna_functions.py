def dna_validator(nucleic_acid):
    """confirms the entered string only contains T,G,C,A base pairs"""
    stringlength = len(nucleic_acid)
    check =  nucleic_acid.count('A') + nucleic_acid.count('T') \
    + nucleic_acid.count('G') + nucleic_acid.count('C')
    if stringlength == check:
        return True
    else:
        return False

def rna_validator(nucleic_acid):
    """confirms the entered string only contains U,G,C,A base pairs"""
    stringlength = len(nucleic_acid)
    check =  nucleic_acid.count('A') + nucleic_acid.count('U') \
    + nucleic_acid.count('G') + nucleic_acid.count('C')
    if stringlength == check:
        return True
    else:
        return False


def convert_dna_to_rna(DNA_STRING):
    """converts a DNA string into an RNA String"""
    dnastring = DNA_STRING.upper()
    assert dna_validator(dnastring),\
        'has invalid characters, please make sure string contains only T, G, C, A basepairs'
    rna = []
    for dna in dnastring:
        if dna == 'T':
            rna.append('U')
        elif dna == '\n':
            rna.append('\n')
        else:
            rna.append(dna)

    rnastring = ''.join(rna)
    return rnastring

def dna_reverse_compliment(DNA_STRING):
    """reverses and prints nucleic acid compliment"""
    dnastring = DNA_STRING.upper()
    assert dna_validator(dnastring),\
        'has invalid characters, please make sure string contains only T, G, C, A basepairs'
    reverse = dnastring[::-1]
    dnacompliment = []
    for dna in reverse:
        if dna == 'A':
            dnacompliment.append('T')
        if dna == 'T':
            dnacompliment.append('A')
        if dna == 'G':
            dnacompliment.append('C')
        if dna == 'C':
            dnacompliment.append('G')
        if dna == '\n':
            dnacompliment.append('\n')
    reversecompliment = ''.join(dnacompliment)
    return reversecompliment

def dna_compliment(DNA_STRING):
    """prints nucleic acid compliment"""
    dnastring = DNA_STRING.upper()
    assert dna_validator(dnastring),\
        'has invalid characters, please make sure string contains only T, G, C, A basepairs'
    dnacompliment = []
    for dna in dnastring:
        if dna == 'A':
            dnacompliment.append('T')
        if dna == 'T':
            dnacompliment.append('A')
        if dna == 'G':
            dnacompliment.append('C')
        if dna == 'C':
            dnacompliment.append('G')
        if dna == '\n':
            dnacompliment.append('\n')
    reversecompliment = ''.join(dnacompliment)
    return reversecompliment

def dna_to_protein(DNA_STRING):
    """converts a dna string into a rna string and returns
    a protein string from that rna string only returns the first frame"""
    dnastring = DNA_STRING.upper()
    assert dna_validator(dnastring),\
        'has invalid characters, please make sure string contains only T, G, C, A basepairs'
    rnastring = convert_dna_to_rna(dnastring)
    assert rna_validator(rnastring),\
        'has invalid characters, please make sure string contains only U, G, C, A basepairs'
    return rna_to_protein_first_frame(rnastring)

def rna_to_protein_first_frame(RNA_STRING):
    """converts RNA string into a protein string"""
    from re import findall
    rnastring = RNA_STRING.upper()
    assert rna_validator(rnastring),\
        'has invalid characters, please make sure string contains only U, G, C, A basepairs'
    codons = findall('...', rnastring)
    amino_acid = []

    RNA_CODON_TABLE = {
    'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
    'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
    'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
    'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
    'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
    'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
    'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'UAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'UAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
    'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'UGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}

    for codon in codons:
        if RNA_CODON_TABLE[codon] == 'Stop':
            break
        elif codon == '\n':
            amino_acid.append('\n')
            
        else:
            amino_acid.append(RNA_CODON_TABLE[codon])

    protein_string = ''.join(amino_acid)
    return protein_string

def rna_to_protein_second_frame(RNA_STRING):
    """converts RNA string into a protein string"""
    from re import findall
    rnastring = RNA_STRING.upper()
    assert rna_validator(rnastring),\
        'has invalid characters, please make sure string contains only U, G, C, A basepairs'
    codons = findall('...', rnastring[1:])
    amino_acid = []

    RNA_CODON_TABLE = {
    'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
    'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
    'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
    'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
    'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
    'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
    'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'UAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'UAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
    'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'UGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}

    for codon in codons:
        if RNA_CODON_TABLE[codon] == 'Stop':
            break
        elif codon == '\n':
            amino_acid.append('\n')
            
        else:
            amino_acid.append(RNA_CODON_TABLE[codon])

    protein_string = ''.join(amino_acid)
    return protein_string

def rna_to_protein_third_frame(RNA_STRING):
    """converts RNA string into a protein string"""
    from re import findall
    rnastring = RNA_STRING.upper()
    assert rna_validator(rnastring),\
        'has invalid characters, please make sure string contains only U, G, C, A basepairs'
    codons = findall('...', rnastring[2:])
    amino_acid = []

    RNA_CODON_TABLE = {
    'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
    'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
    'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
    'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
    'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
    'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
    'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'UAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'UAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
    'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'UGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}

    for codon in codons:
        if RNA_CODON_TABLE[codon] == 'Stop':
            break
        elif codon == '\n':
            amino_acid.append('\n')
            
        else:
            amino_acid.append(RNA_CODON_TABLE[codon])

    protein_string = ''.join(amino_acid)
    return protein_string

def rna_to_protein_6_frames(RNA_STRING):
    """converts RNA string into a protein string and prints 6 the frames
    3 from frames from unreserved rna string and 3 from reversed dna frame in logical order
    1) [:]
    2) [1:]
    3) [2:]
    4) reversed[:]
    5) reversed[1:]
    6) reversed[2:]"""
    from re import findall
    rnastring = RNA_STRING.upper()
    assert rna_validator(rnastring), \
        'has invalid characters, please make sure string contains only U, G, C, A basepairs'

    RNA_CODON_TABLE = {
        'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
        'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
        'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
        'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
        'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
        'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
        'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
        'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
        'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
        'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
        'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
        'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
        'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
        'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
        'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
        'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
    }

    protein = []
    for i in xrange(0, 3):
        codons = findall('...', rnastring[i:])
        for codon in codons:
            if RNA_CODON_TABLE[codon] == 'Stop':
                break
            elif codon == '\n':
                protein.append('\n')
            else:
                protein.append(RNA_CODON_TABLE[codon])
        print ''.join(protein)
        protein = []

    revprotein = []
    revrnastring = rnastring[::-1]
    for j in xrange(0, 3):
        codons = findall('...', revrnastring[j:])
        for revcodon in codons:
            if RNA_CODON_TABLE[revcodon] == 'Stop':
                break
            elif revcodon == '\n':
                revprotein.append('\n')
            else:
                revprotein.append(RNA_CODON_TABLE[revcodon])
        print ''.join(revprotein)
        revprotein = []


def findalloverlap(pattern, target):
    """finds all occurrences of given pattern within a given target"""
    count = target.find(pattern)

    while count > -1:
        print count + 1
        count += 1
        count = target.find(pattern, count)

        
def compare_all_kmer_of_given_length(target_string, kmer_length):
    from collections import OrderedDict
    """prints all the k-mers of a given length with
    the frequency the in which the k-mers appear"""
    seq = target_string
    k = kmer_length
    kmers = {}
    for i in xrange(len(seq) - k + 1):
        kmer = seq[i:i + k]
        if kmers.has_key(kmer):
            kmers[kmer] += 1
        else:
            kmers[kmer] = 1
    sorted_kmers = OrderedDict(sorted(kmers.items(), key=lambda x: x[1]))
    for kmer, count in sorted_kmers.items():
        print("%s: %s" % (kmer, count))

def most_frequent_kmer(taget_string, target_kmer_length):
    """prints the most frequent k-mer of
     length specified length"""
    kmerstring = taget_string
    k = target_kmer_length

    kmer_dict = dict()

    for i in xrange(len(kmerstring) - k + 1):
        if kmerstring[i:i + k] in kmer_dict:
            kmer_dict[kmerstring[i:i + k]] += 1
        else:
            kmer_dict[kmerstring[i:i + k]] = 1
    most_frequent_kmer = [item[0] for item in kmer_dict.items() if item[1] == max(kmer_dict.values())]
    print str(most_frequent_kmer).replace(',', '').replace("'", '')[1:-1]



