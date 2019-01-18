#!/usr/bin/env python

''' 
 * All rights Reserved, Designed By HIT-Bioinformatics   
 * @Title:  divide.py
 * @Description: Divide Protein Alignment files
 * @author: fuyilei96
 * @date: December 21 2018
 * @version V4.0.0   
'''

import sys
import argparse
import os

def findposition(one_protein):
    poslist = []
    lengthlist = []
    count = 0
    i = 0
    # print(len(one_protein))
    while(i < len(one_protein) - 1):
        if one_protein[i] == '-':
            poslist.append(i)
            count = 1
            i = i + 1
            while(one_protein[i] == "-"):
                count = count+1
                i = i + 1
                if i == len(one_protein):
                    break
            lengthlist.append(count)
        i = i + 1
    # longest = max(lengthlist)
    # longestpos = poslist[lengthlist.index(longest)]
    return (poslist, lengthlist)

def whole_protein_list(proteinlist):
    data = []
    for i in proteinlist:
        data.append(findposition(i))
    return data

def index_withoutexception(self,i):
    try:
        return self.index(i)
    except:
        return -1

def calctimes(data):
    poslist = []
    for i in data:
        for j in i[0]:
            poslist.append(j)
    poslist = sorted(list(set(poslist)))
    timeslist = [0]*len(poslist)
    for i in data:
        for j in i[0]:
            if index_withoutexception(poslist, j) != -1:
                timeslist[index_withoutexception(poslist, j)] = timeslist[index_withoutexception(poslist, j)] + 1
                
    sumlist = [0]*len(poslist)
    for i in range(len(poslist)):
        for j in data:
            if poslist[i] in j[0]:
                sumlist[i] = sumlist[i] + j[1][j[0].index(poslist[i])]
    scorelist = []
    for i in range(len(poslist)):
        scorelist.append(timeslist[i]*sumlist[i])
    return (poslist, timeslist, sumlist, scorelist)

def find_division_pos_score(poslen_detail, proteinlist):
    protein_part0 = []
    protein_part1 = []
    protein_part2 = []
    first_score = 0
    first_pos = 0
    second_score = 0
    second_pos = 0
    for i in range(len(poslen_detail[0])):
        if poslen_detail[3][i] > first_score:
            first_score = poslen_detail[3][i]
            first_pos = poslen_detail[0][i]
    for i in range(len(poslen_detail[0])):    
        if poslen_detail[3][i] > second_score and poslen_detail[3][i] < first_score:
            second_score = poslen_detail[3][i]
            second_pos = poslen_detail[0][i]
            
    if first_pos > second_pos:
        temp_pos = first_pos
        first_pos = second_pos
        second_pos = temp_pos
        temp_score = first_score
        first_score = second_score
        second_score = temp_score
    for i in proteinlist:
        protein_part0.append(i[0:first_pos])
        protein_part1.append(i[first_pos:second_pos])
        protein_part2.append(i[second_pos:])
    return (protein_part0, protein_part1, protein_part2)



#Arg parser for this program
parser = argparse.ArgumentParser(description = "Divide file from original path to destination path.")
parser.add_argument('-orf', '--originalfilepath', type = str, help = "The file path of original file path")
parser.add_argument('-ouf' ,'--outputfilepath', type = str, help = "The file path of output file path")
# parser.add_argument('-fp' ,'--first_proportion', type = float, help = "The first proportion to cut the file, should be less than 1")
# parser.add_argument('-sp' ,'--second_proportion', type = float, help = "The second proportion to cut the file, should be less than 1")
args = parser.parse_args()

#Some paths...
#/home/fuyilei96/ProteinAlignment/proteinalignment/divided/sabre/
originalfilepath = args.originalfilepath
outputfilepath = args.outputfilepath
temp_path = outputfilepath + "temp/"
_in_file_path = temp_path
_out_file_path = outputfilepath
output_path = outputfilepath + "output/"
# first_pt = args.first_proportion
# second_pt = args.second_proportion

#Make dictionary for those paths.
os.system("mkdir " + temp_path)
os.system("mkdir " + outputfilepath + "out_pt0 "  + outputfilepath + "out_pt1 "  + outputfilepath + "out_pt2 ")
os.system("mkdir "  + _out_file_path + "in_pt0 " + _out_file_path + "in_pt1 " + _out_file_path + "in_pt2 ")
os.system("mkdir " + output_path)


#First alignment using msaprobs, outputing to temp folder
files = os.listdir(originalfilepath)
for _filename in files:
    os.system("cd " + originalfilepath + " && " + "msaprobs -o " + temp_path + _filename + "_aligned" + " " + _filename)


#Second alignmentS
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
    #Divide file with preseted proportion.
    divided = find_division_pos_score(calctimes(whole_protein_list(protein)), protein)
    tempstring = []




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
    #If there is only one sequence in alignment file, msaprobs do not recogonize the file as an illegal input.
    #Generate aligned file without using msaprobs
    if empty_flag_0.count(0) == 1:
        with open(pt0_outpath + originalfname + "_pt0_aligned", "w") as file:
            file.write(nametemp)
            file.write(linetemp)
    else:
        #Generate aligned file using msaprobs
        os.system("msaprobs -o " + pt0_outpath + originalfname + "_pt0_aligned " + _out_file_path + "in_pt0/" + originalfname + "_pt0")

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
    #If there is only one sequence in alignment file, msaprobs do not recogonize the file as an illegal input.
    #Generate aligned file without using msaprobs
    if empty_flag_1.count(0) == 1:
        with open(pt1_outpath + originalfname + "_pt1_aligned", "w") as file:
            file.write(nametemp)
            file.write(linetemp)
    else:
        #Generate aligned file using msaprobs
        os.system("msaprobs -o " + pt1_outpath + originalfname + "_pt1_aligned " + _out_file_path + "in_pt1/" + originalfname + "_pt1")

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
    #If there is only one sequence in alignment file, msaprobs do not recogonize the file as an illegal input.
    #Generate aligned file without using msaprobs
    if empty_flag_2.count(0) == 1:
        with open(pt2_outpath + originalfname + "_pt2_aligned", "w") as file:
            file.write(nametemp)
            file.write(linetemp)
    else:
        #Generate aligned file using msaprobs
        os.system("msaprobs -o " + pt2_outpath + originalfname + "_pt2_aligned " + _out_file_path + "in_pt2/" + originalfname + "_pt2")

    #Combining generated re-aligned files...
    protein0 = []
    protein1 = []
    protein2 = []
    protein_n = []

    with open(pt0_outpath + originalfname + "_pt0_aligned", "r") as file0:
            with open(pt1_outpath + originalfname + "_pt1_aligned", "r") as file1:
                with open(pt2_outpath + originalfname + "_pt2_aligned", "r") as file2:
                    with open(output_path + originalfname + "_aligned", "a") as optfile:
                        while(1):
                            #Dealing with line feed
                            line0 = file0.readline()
                            if not line0:
                                break
                            elif line0[0] == '>':
                                protein_n.append(line0[:-1])
                                protein0.append(''.join(tempstring))
                                tempstring = []
                            else:
                                tempstring.append(line0[:-1])
                        protein0.append(''.join(tempstring))
                        del protein0[0]

                        if len(protein0) > 0:
                            len_of_protein0 = len(protein0[0])
                            for i in range(len(empty_flag_0)):
                                #Insert sequences with all spaces.
                                if empty_flag_0[i] == 1:
                                    protein_n.insert(i, original_protein_n[i])
                                    protein0.insert(i, "-"*len_of_protein0)
                        else:
                            for i in range(len(empty_flag_0)):
                                protein_n.insert(i, original_protein_n[i])

                        while(1):
                            line1 = file1.readline()
                            if not line1:
                                break
                            elif line1[0] == '>':
                                protein1.append(''.join(tempstring))
                                tempstring = []
                            else:
                                tempstring.append(line1[:-1])
                        protein1.append(''.join(tempstring))
                        del protein1[0]
                        if len(protein1) > 0:
                            len_of_protein1 = len(protein1[0])
                            for i in range(len(empty_flag_0)):
                                if empty_flag_1[i] == 1:
                                    protein1.insert(i, "-"*len_of_protein1)


                        while(1):
                            line2 = file2.readline()
                            # print(line2)
                            if not line2:
                                break
                            elif line2[0] == '>':
                                protein2.append(''.join(tempstring))
                                tempstring = []
                            else:
                                tempstring.append(line2[:-1])
                        protein2.append(''.join(tempstring))
                        # print(protein2)
                        del protein2[0]
                        if len(protein2) > 0:
                            len_of_protein2 = len(protein2[0])
                            for i in range(len(empty_flag_0)):
                                if empty_flag_2[i] == 1:
                                    protein2.insert(i, "-"*len_of_protein2)
                        #File Combanation
                        for i in range(len(protein_n)):
                            optfile.write(protein_n[i]+'\n')
                            if len(protein0) > 0 and  len(protein1) > 0 and len(protein2) > 0:
                                optfile.write(protein0[i]+protein1[i]+protein2[i]+'\n')
                            elif len(protein0) > 0 and  len(protein1) > 0 :
                                optfile.write(protein0[i]+protein1[i]+'\n')
                            elif len(protein1) > 0 and len(protein2) > 0:
                                optfile.write(protein1[i]+protein2[i]+'\n')
                            elif len(protein0) > 0  and len(protein2) > 0:
                                optfile.write(protein0[i]+protein2[i]+'\n')
    # print(empty_flag_0, empty_flag_1, empty_flag_2)
    # print(protein0)
    # print(protein1)
    # print(protein2)
    # break