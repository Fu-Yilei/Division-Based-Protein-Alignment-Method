#!/usr/bin/env python

''' 
 * All rights Reserved, Designed By HIT-Bioinformatics   
 * @Title:  score.py
 * @Description: Score after having the output
 * @author: fuyilei96
 * @date: December 21 2018
 * @version V1.0.0   
'''

import sys
import argparse
import os

parser = argparse.ArgumentParser(description = "Score combined files")
parser.add_argument('-af', '--alignedfilepath', type = str, help = "The file path of aligned file path")
parser.add_argument('-rf', '--referencefilepath', type = str, help = "The file path of reference file path")
parser.add_argument('-op', '--outputpath', type = str, help = "The file path of output file path")
parser.add_argument('-dbn', '--databasename', type = str, help = "The name of database")
args = parser.parse_args()

aligned_file_path = args.alignedfilepath
reference_file_path = args.referencefilepath
database_name = args.databasename
outpath = args.outputpath
os.system("mkdir " + outpath)
aligned_filenames = os.listdir(aligned_file_path)
for _filename in aligned_filenames:
    os.system("qscore -test " + aligned_file_path + _filename + " -ref " + reference_file_path + _filename[:-8] + " >> " + outpath + database_name + "_score")