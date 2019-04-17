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
parser.add_argument('-rt' ,'--refinementtimes', type = str, help = "refinement times")


args = parser.parse_args()

#Some paths...
#/home/fuyilei96/ProteinAlignment/proteinalignment/divided/sabre/
originalfilepath = args.originalfilepath
outputfilepath = args.outputfilepath
temp_path = outputfilepath + "temp/"
refinement_path = outputfilepath + "refinement/"
_in_file_path = temp_path
_out_file_path = outputfilepath
output_path = outputfilepath + "output/"
first_fraction = args.firstfraction
second_fraction = args.secondfraction
refinementtime = args.refinementtimes


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
        os.system("cd " + originalfilepath + " && " + "probcons "  + _filename + ">>" + refinement_path + _filename + "_aligned -ir " + refinementtime )

############################################################################################################################

