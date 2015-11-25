__author__ = 'marcsantago'

'''A ROSALIND bioinformatics script to extract sequence information FASTA format data.'''

import urllib
import contextlib

def ReadFASTA(data_location):
        '''Determines the data type of the FASTA format data and passes the appropriate information to be parsed.'''

        # If given a list, return fasta information from all items in the list.
        if type(data_location) == list:
                fasta_list =[]
                for location in data_location:
                        fasta_list+=ReadFASTA(location)
                return fasta_list


        # Check for a text file, return fasta info from the text file.
        if data_location[-4:] == '.txt':
                with open(data_location) as f:
                        return ParseFASTA(f)

        # Check for a website, return fasta info from the website.
        elif data_location[0:4] == 'http':
                with contextlib.closing(urllib.urlopen(data_location)) as f:
                        return ParseFASTA(f)


def ParseFASTA(f):
        '''Extracts the Sequence Name and Nucleotide/Peptide Sequence from the a FASTA format file or website.'''
        fasta_list=[]
        for line in f:

                # If the line starts with '>' we've hit a new DNA strand, so append the old one and create the new one.
                if line[0] == '>':

                        # Using try/except because intially there will be no current DNA strand to append.
                        try:
                                fasta_list.append(current_dna)
                        except UnboundLocalError:
                                pass

                        current_dna = [line.lstrip('>').rstrip('\n'),'']

                # Otherwise, append the current DNA line to the current DNA
                else:
                        current_dna[1] += line.rstrip('\n')

        # Append the final DNA strand after reading all the lines.
        fasta_list.append(current_dna)

        return fasta_list


def MergeMaxOverlap(str_list):
    '''Given a list of strings, returns the list of strings with the two strings having maximum overlap merged into a single string.'''
    max_length = -1

    for prefix_index in xrange(len(str_list)):
        # Don't compare a string with itself.
        for suffix_index in [num for num in range(len(str_list)) if num != prefix_index]:
            # Name the two selected strings for code readability.
            prefix, suffix = str_list[prefix_index], str_list[suffix_index]
            # Begin finding the maximum overlap between the prefix and suffix strings.
            i = 0
            while prefix[i:] != suffix[0:len(prefix[i:])]:
                i += 1
            # Store the overlap length and string indicies if they the longest thus far.
            if len(prefix) - i > max_length:
                max_length = len(prefix) - i
                max_indicies = [prefix_index, suffix_index]

    # Return all strings without maximum overlap, and the merged string with maximum overlap.
    return [str_list[j] for j in range(len(str_list)) if j not in max_indicies] + [
        str_list[max_indicies[0]] + str_list[max_indicies[1]][max_length:]]


def LongestCommonSuperstring(str_list):
    '''Return the longest common superstring from a list of strings.'''
    # Note: In general, not necessarily the longest but a good approximation at worst.
    # For the Rosalind problem we're given the condition that there exists a unique way to reconstruct the entire chromosome from these reads by gluing
    # together pairs of reads that overlap by more than half their length, so this method should be optimal.

    # Repeatedly find the merge strings with the maximum overlap until we have one string.
    while len(str_list) > 1:
        str_list = MergeMaxOverlap(str_list)

    return str_list[0]


if __name__ == '__main__':
    dna_list = [fasta[1] for fasta in ReadFASTA('genomeseq.txt')]
    super_string = LongestCommonSuperstring(dna_list)

    print super_string
    '''with open('answer.txt', 'w') as output_data:
        output_data.write(super_string)'''