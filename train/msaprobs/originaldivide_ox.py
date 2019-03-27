import os

tp = "/data3/fuyilei96/ProteinTest/msaprobs/sabre/_ff_0.15_sf_0.8/temp/"
rp = "/home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/ref/"
os.system("mkdir /data3/fuyilei96/ProteinTest/msaprobs/sabre/_ff_0.15_sf_0.8/")
os.system("mkdir /data3/fuyilei96/ProteinTest/msaprobs/sabre/_ff_0.15_sf_0.8/temp_divided/")

tpfilelist = os.listdir(tp)
tpout = "/data3/fuyilei96/ProteinTest/msaprobs/sabre/_ff_0.15_sf_0.8/temp_divided/"

def divide_by_fraction(protein, first_fraction, second_fraction):
    first_pos = int(float(len(protein[0])) * first_fraction)
    second_pos = int(float(len(protein[0])) * second_fraction)

    protein_part0 = []
    protein_part1 = []
    protein_part2 = []
    for i in protein:
        protein_part0.append(i[0:first_pos])
        protein_part1.append(i[first_pos:second_pos])
        protein_part2.append(i[second_pos:])
        
    return (protein_part0, protein_part1, protein_part2)



for f in tpfilelist:
    original_protein_n = []
    protein = []
    tempstring = []
    with open(tp + f, "r") as file:
        while(1):
            line = file.readline()
            if not line:
                break
            elif line[0] == '>':
                original_protein_n.append(line[:-1])
                protein.append(''.join(tempstring))
                tempstring = []
            else:
                tempstring.append(line[:-1])
        protein.append(''.join(tempstring))
    del protein[0]
    ######################################################
    #Divide file with preseted proportion.
    divided = divide_by_fraction(protein, 0.15, 0.8)

    with open(tpout+f, 'w') as file:
        for i in range(len(original_protein_n)):
            name = original_protein_n[i] + '\n'
            line = divided[1][i] + '\n'
            file.write(name)
            file.write(line)