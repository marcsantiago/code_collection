import re

def dna_to_rna(string):
    dnastring = string
    rna = []
    for dna in dnastring:
        if dna == 'A':
            rna.append('U')
        if dna == 'T':
            rna.append('A')
        if dna == 'G':
            rna.append('C')
        if dna == 'C':
            rna.append('G')
    rnastring = ''.join(rna)
    return rnastring


def dna_reverse_compliment(string):
    dnastring = string
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
    reversecompliment = ''.join(dnacompliment)
    return reversecompliment


def rna_to_protein(string):
    rnastring = string
    codon = re.findall('...', rnastring)
    aminoAcid = []

    #need to come up with an easier way to test for amino acids
    for acid in codon:
        if acid == 'UAA' or acid == 'UAG' or acid == 'UGA':  #Stop codon
            break
        elif acid == 'GGU' or acid == 'GGC' or acid == 'GGA' or acid == 'GGG':  #Glycine
            aminoAcid.append('G')
        elif acid == 'GCU' or acid == 'GCC' or acid == 'GCA' or acid == 'GCG':  #Alanine
            aminoAcid.append('A')
        elif acid == 'GUU' or acid == 'GUC' or acid == 'GUA' or acid == 'GUG':  #Valine
            aminoAcid.append('V')
        elif acid == 'UUA' or acid == 'UUG' or acid == 'CUU' or acid == 'CUC' or acid == 'CUA' or acid == 'CUG':  #Leucine
            aminoAcid.append('L')
        elif acid == 'AUU' or acid == 'AUC' or acid == 'AUA':  #Isoleucine
            aminoAcid.append('I')
        elif acid == 'CCU' or acid == 'CCC' or acid == 'CCA' or acid == 'CCG':  #Proline
            aminoAcid.append('P')
        elif acid == 'UUU' or acid == 'UUC':  #Phenylalanine
            aminoAcid.append('F')
        elif acid == 'UAU' or acid == 'UAC':  #Tyrosine
            aminoAcid.append('Y')
        elif acid == 'UGG':  #Trytophan
            aminoAcid.append('W')
        elif acid == 'UCU' or acid == 'UCC' or acid == 'UCA' or acid == 'UCG' or acid == 'AGU' or acid == 'AGC':  #Serine
            aminoAcid.append('S')
        elif acid == 'ACU' or acid == 'ACC' or acid == 'ACA' or acid == 'ACG':  #Threorine
            aminoAcid.append('T')
        elif acid == 'UGU' or acid == 'UGC':  #Cyteine
            aminoAcid.append('C')
        elif acid == 'AUG':  #Methionine
            aminoAcid.append('M')
        elif acid == 'AAU' or acid == 'AAC':  #Asparagine
            aminoAcid.append('N')
        elif acid == 'CAA' or acid == 'CAG':  #Glutamine
            aminoAcid.append('Q')
        elif acid == 'AAA' or acid == 'AAG':  #Lysine
            aminoAcid.append('K')
        elif acid == 'CGU' or acid == 'CGC' or acid == 'CGA' or acid == 'CGG' or acid == 'AGA' or acid == 'AGG':  #Arginine
            aminoAcid.append('R')
        elif acid == 'CAU' or acid == 'CAC':  #Histidine
            aminoAcid.append('H')
        elif acid == 'GAU' or acid == 'GAC':  #Aspartate
            aminoAcid.append('D')
        elif acid == 'GAA' or acid == 'GAG':  #Glutamate
            aminoAcid.append('E')
    sAcid = ''.join(aminoAcid)
    return sAcid

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


def parse_dna_from_fasta_file(filename):
    myfile = open(filename)
    seq = []
    for lines in myfile:
        if not lines.startswith('>'):
            seq.append(lines)
    mysequences = "".join(seq)
    del seq
    return mysequences


