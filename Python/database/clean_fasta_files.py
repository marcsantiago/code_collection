#!/usr/bin/env
__author__ = 'marcsantiago'


def get_file_names():
    import os
    for i in os.listdir('fastafiles'):
        if i.endswith('.fasta'):
            yield i

def clean_fasta_files():
    import os
    for files in get_file_names():
        path = 'fastafiles/' + files
        with open(path, 'r') as fasta_read:
            file = fasta_read.read().replace('comp', '>'+files+'_comp')

        finish_path = 'fastafiles/' + files.replace('Done', 'Clean')
        with open(finish_path, 'w') as fasta_write:
            fasta_write.write(file)
        os.remove(path)




