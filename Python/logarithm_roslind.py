from math import log10


def gc_at_content(dna_sequence):
	gc = dna_sequence.count("G") + dna_sequence.count("C")
	at = len(dna_sequence) - gc
	return gc, at

def calculate_log(number_of_gc, number_of_at, logarithm_values):
	return log10(((logarithm_values / 2) ** number_of_gc) * ((.5 - logarithm_values /2) ** number_of_at))


with open('rosalind_prob.txt', 'r') as indata:
	sequence, log_list = indata.readlines()

log_list = [float(i) for i in log_list.strip().split()]
gc_num, at_num = gc_at_content(sequence.strip())

logs = []
for element in log_list:
	logs.append(round(calculate_log(gc_num, at_num, element), 3))
	# logs.append(calculate_log(gc_num, at_num, element))

with open('log_out.txt', 'w') as outdata:
	outdata.write(" ".join([str(i) for i in logs]))
