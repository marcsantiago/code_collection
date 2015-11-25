junkfilename = 'junk_output.txt'
with open(junkfilename, 'w') as junk_output:
    with open('rosalind_cons.txt', 'r') as data: 
        for line in data.readlines():
            if line.startswith('>'):
                junk_output.write('\n'+line)
                continue
            else:
                junk_output.write(line.strip())

with open('junk_output.txt', 'r') as data:
     dna_lines = [str(i).strip() for i in data.readlines() if not i.startswith(">")]
     dna_lines = filter(None, dna_lines)

a_list = []
t_list = []
g_list = []
c_list = []
consensus = []
index = 0
while index < len(dna_lines[0]): 
    a_num = 0
    t_num = 0
    c_num = 0
    g_num = 0
    for element in dna_lines:
        if element[index] == "A":
            a_num += 1

        elif element[index] == "T":
            t_num += 1

        elif element[index] == "C":
            c_num += 1

        elif element[index] == "G":
            g_num += 1
    
    if a_num == max(a_num, t_num, c_num, g_num):
        consensus.append("A")
    
    elif t_num == max(a_num, t_num, c_num, g_num):
        consensus.append("T")

    elif g_num == max(a_num, t_num, c_num, g_num):
        consensus.append("G")

    elif c_num == max(a_num, t_num, c_num, g_num):
        consensus.append("C")

    a_list.append(a_num)
    t_list.append(t_num)
    c_list.append(c_num)
    g_list.append(g_num)
    index += 1

with open("consensusdata.txt", 'w') as outdata:
    outdata.write("".join(consensus) + "\n")
    outdata.write("A: %s" % " ".join([str(i) for i in a_list]) + "\n")
    outdata.write("C: %s" % " ".join([str(i) for i in c_list]) + "\n")
    outdata.write("G: %s" % " ".join([str(i) for i in g_list]) + "\n")
    outdata.write("T: %s" % " ".join([str(i) for i in t_list]))

# print("".join(consensus))
# print("A: %s" % " ".join([str(i) for i in a_list]))
# print("C: %s" % " ".join([str(i) for i in c_list]))
# print("G: %s" % " ".join([str(i) for i in g_list]))
# print("T: %s" % " ".join([str(i) for i in t_list]))