#! /usr/bin/env python2.7
__author__ = 'marcsantiago'


def gene_position_list():
    with open("SOS_set13_181g_55t.charset", "r") as gene_file:
        gene_data = gene_file.readlines()

    position_list = []
    master_position_list = []
    for line in gene_data:
        gene_line = str(line).strip()
        find_equal_sign = gene_line.find("=")
        find_minus_sign = gene_line.find("-")
        position_list.append(gene_line[find_equal_sign + 2:find_minus_sign])
        position_list.append(gene_line[find_minus_sign + 2:-1])
        master_position_list.append(position_list)
        position_list = []
    return master_position_list