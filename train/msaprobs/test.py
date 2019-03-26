#!/usr/bin/env python

''' 
 * All rights Reserved, Designed By HIT-Bioinformatics   
 * @Title:  divide.py
 * @Description: Divide Protein Alignment files
 * @author: fuyilei96
 * @date: December 21 2018
 * @version V5.0.0   
'''

import sys
import argparse
import os




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




#Arg parser for this program
parser = argparse.ArgumentParser(description = "Divide file from original path to destination path.")
parser.add_argument('-orf', '--originalfilepath', type = str, help = "The file path of original file path")
parser.add_argument('-ouf' ,'--outputfilepath', type = str, help = "The file path of output file path")
parser.add_argument('-ff', '--firstfraction', type = float, help = "First fraction, scale 0-second fraction")
parser.add_argument('-sf' ,'--secondfraction', type = float, help = "Second fraction, scale First Fraction-1")


args = parser.parse_args()

#Some paths...
#/home/fuyilei96/ProteinAlignment/proteinalignment/divided/sabre/
originalfilepath = args.originalfilepath
outputfilepath = args.outputfilepath
temp_path = outputfilepath + "temp/"
_in_file_path = temp_path
_out_file_path = outputfilepath
output_path = outputfilepath + "output/"
first_fraction = args.firstfraction
second_fraction = args.secondfraction

#Make dictionary for those paths.
os.system("mkdir " + temp_path)
os.system("mkdir " + outputfilepath + "out_pt0 "  + outputfilepath + "out_pt1 "  + outputfilepath + "out_pt2 ")
os.system("mkdir "  + _out_file_path + "in_pt0 " + _out_file_path + "in_pt1 " + _out_file_path + "in_pt2 ")
os.system("mkdir " + output_path)

############################################################################################################################

#First alignment using msaprobs, outputing to temp folder
files = os.listdir(originalfilepath)
if not os.listdir(temp_path):
    for _filename in files:
        os.system("cd " + originalfilepath + " && " + "msaprobs -o " + temp_path + _filename + "_aligned" + " " + _filename)

############################################################################################################################


#Second alignment
files = os.listdir(_in_file_path)
for _filename in files:
    # _filename = "sup_043_aligned"
    original_protein_n = []
    protein = []
    tempstring = []
    #Reading each file, deal with msaprobs' line feed strategy.
    with open(_in_file_path +_filename, "r") as file:
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
    divided = divide_by_fraction(protein, first_fraction, second_fraction)
    tempstring = []

    ######################################################

    #Doing alignment on divided files.
    if _filename[-8:] == "_aligned":
        originalfname = _filename[:-8]
    empty_flag_0 = []
    empty_flag_1 = []
    empty_flag_2 = []
    pt0_outpath = _out_file_path + "out_pt0/"
    pt1_outpath = _out_file_path + "out_pt1/"
    pt2_outpath = _out_file_path + "out_pt2/"


    with open(_out_file_path + "in_pt0/"+originalfname+"_pt0", 'w') as file:
        empty_flag_0 = [0] * len(original_protein_n)
        for i in range(len(original_protein_n)):
            name = original_protein_n[i] + '\n'
            #Removing spaces, which is '-' in alignment file
            line = divided[0][i].replace('-', '') + '\n'
            if line == '\n':
                empty_flag_0[i] = 1
            else:
                file.write(name)
                file.write(line)
                nametemp = name
                linetemp = line

    with open(_out_file_path + "in_pt1/"+originalfname+"_pt1", 'w') as file:
        empty_flag_1 = [0] * len(original_protein_n)
        for i in range(len(original_protein_n)):
            name = original_protein_n[i] + '\n'
            line = divided[1][i].replace('-', '') + '\n'
            if line == '\n':
                empty_flag_1[i] = 1
            else:
                file.write(name)
                file.write(line)
                nametemp = name
                linetemp = line

    with open(_out_file_path + "in_pt2/"+originalfname+"_pt2", 'w') as file:
        empty_flag_2 = [0] * len(original_protein_n)
        for i in range(len(original_protein_n)):
            name = original_protein_n[i] + '\n'
            line = divided[2][i].replace('-', '') + '\n'
            if line == '\n':
                empty_flag_2[i] = 1
            else:
                file.write(name)
                file.write(line)
                nametemp = name
                linetemp = line
