#!/usr/bin/env python


import sys
import argparse
import os


# os.system("python divide.py -orf /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/proteinalignment/benchmark/ox/in/ -ouf /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/msaprobs/ox/ ")


#Some paths...

originalfilepath = "/mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/proteinalignment/benchmark/ox/in/"
outputfilepath = "/mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/msaprobs/ox/"
temp_path = outputfilepath + "temp/"
_in_file_path = temp_path
_out_file_path = outputfilepath
output_path = outputfilepath + "output/"
# first_pt = args.first_proportion
# second_pt = args.second_proportion
os.system("mkdir  /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/msaprobs/sabre /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/msaprobs/ox /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/msaprobs/bali3")

#Make dictionary for those paths.
os.system("mkdir " + temp_path)
os.system("mkdir " + outputfilepath + "out_pt0 "  + outputfilepath + "out_pt1 "  + outputfilepath + "out_pt2 ")
os.system("mkdir "  + _out_file_path + "in_pt0 " + _out_file_path + "in_pt1 " + _out_file_path + "in_pt2 ")
os.system("mkdir " + output_path)




#First alignment using msaprobs, outputing to temp folder
files = os.listdir(originalfilepath)
for _filename in files:
    os.system("cd " + originalfilepath + " && " + "msaprobs -o " + temp_path + _filename + "_aligned" + " " + _filename)

