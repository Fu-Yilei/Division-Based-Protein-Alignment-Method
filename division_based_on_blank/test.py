#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataSciece.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'division_based_on_blank'))
	print(os.getcwd())
except:
	pass

#%%
import os
import sys
import numpy as np


#%%
path = "../../divided/sabre/temp/"
files = os.listdir(path)


#%%
files[0]


#%%
original_protein_n = []
protein = []
tempstring = []
with open(path+files[0], 'r') as file:
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


#%%
protein


#%%
def findlongest(one_protein):
    poslist = []
    lengthlist = []
    count = 0
    i = 0
    while(i < len(one_protein)):
        if one_protein[i] == '-':
            poslist.append(i)
            count = 1
            i = i + 1
            while(one_protein[i] == "-"):
                count = count+1
                i = i + 1
            lengthlist.append(count)
        i = i + 1
    longest = max(lengthlist)
    longestpos = poslist[lengthlist.index(longest)]
    return (poslist, lengthlist)


#%%
def whole_protein_list(proteinlist):
    data = []
    for i in proteinlist:
        data.append(findlongest(i))
    return data
data = whole_protein_list(protein)


#%%
data


#%%
def find_division_pos(poslen_detail, proteinlist):
    protein_part0 = []
    protein_part1 = []
    protein_part2 = []
    first_len = 0
    first_pos = 0
    second_len = 0
    second_pos = 0
    for i in poslen_detail:
        for j in range(len(i[1])):
            if i[1][j] > first_len:
                first_len = i[1][j]
                first_pos = i[0][j]
            if i[1][j] > second_len and i[1][j] < first_len:
                second_len = i[1][j]
                second_pos = i[0][j]
    if first_pos > second_pos:
        temp_pos = first_pos
        first_pos = second_pos
        second_pos = temp_pos
        temp_len = first_len
        first_len = second_len
        second_len = temp_len
    for i in proteinlist:
        protein_part0.append(i[0:first_pos])
        protein_part1.append(i[first_pos:second_pos])
        protein_part2.append(i[second_pos:])
    return (protein_part0, protein_part1, protein_part2)
    
find_division_pos(data, protein)    


#%%
def division(whole_protein, first_proportion, second_proportion):
    #This is a function for dividing files into proportions inputed.
    protein_part_1 = []
    protein_part_2 = []
    protein_part_0 = []
    for i in whole_protein:
        first_position = int(len(i)*first_proportion)
        second_position = int(len(i)*second_proportion)
        protein_part_0.append(i[0:first_position])
        protein_part_1.append(i[first_position:second_position])
        protein_part_2.append(i[second_position:])
    return (protein_part_0, protein_part_1, protein_part_2)


division(protein, 0.2, 0.8)
        


#%%



