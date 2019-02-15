#!/usr/bin/env python


import os


os.system("mkdir /home/fuyilei96/ProteinAlignment/proteinalignment/divided/sabre/ /home/fuyilei96/ProteinAlignment/proteinalignment/divided/bali3 /home/fuyilei96/ProteinAlignment/proteinalignment/divided/ox /home/fuyilei96/ProteinAlignment/proteinalignment/divided/sabre/temp/ /home/fuyilei96/ProteinAlignment/proteinalignment/divided/bali3/temp/ /home/fuyilei96/ProteinAlignment/proteinalignment/divided/ox/temp/")
sabre = "/home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/in/"
sabre_temp = "/home/fuyilei96/ProteinAlignment/proteinalignment/divided/sabre/temp/"
bali3 = "/home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/bali3/in/"
bali3_temp = "/home/fuyilei96/ProteinAlignment/proteinalignment/divided/bali3/temp/"
ox = "/home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/ox/in/"
ox_temp = "/home/fuyilei96/ProteinAlignment/proteinalignment/divided/ox/temp/"

files = os.listdir(sabre)
for _filename in files:
    os.system("cd " + sabre + " && " + "msaprobs -ir 1 -o " + sabre_temp + _filename + "_aligned" + " " + _filename)

files = os.listdir(bali3)
for _filename in files:
    os.system("cd " + bali3 + " && " + "msaprobs  -ir 1 -o " + bali3_temp + _filename + "_aligned" + " " + _filename)


files = os.listdir(ox)
for _filename in files:
    os.system("cd " + ox + " && " + "msaprobs  -ir 1 -o " + ox_temp + _filename + "_aligned" + " " + _filename)