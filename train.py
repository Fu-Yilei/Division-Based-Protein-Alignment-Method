#!/usr/bin/env python

''' 
 * All rights Reserved, Designed By HIT-Bioinformatics   
 * @Title:  train.py
 * @Description: Run program
 * @author: fuyilei96
 * @date: December 21 2018
 * @version V2.0.0   
'''


import sys
import os

for i in range(16, 42, 2):
    j = float(i)/100
    os.system("mkdir  /home/fuyilei96/ProteinAlignment/proteinalignment/divided/sabre /home/fuyilei96/ProteinAlignment/proteinalignment/divided/ox /home/fuyilei96/ProteinAlignment/proteinalignment/divided/bali3")
    os.system("python divide.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/in/ -ouf /home/fuyilei96/ProteinAlignment/proteinalignment/divided/sabre/ -fp " + str(j) + " -sp " + str(1 - j))
    os.system("python divide.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/ox/in/ -ouf /home/fuyilei96/ProteinAlignment/proteinalignment/divided/ox/ -fp " + str(j) + " -sp " + str(1 - j))
    os.system("python divide.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/bali3/in/ -ouf /home/fuyilei96/ProteinAlignment/proteinalignment/divided/bali3/ -fp " + str(j) + " -sp " + str(1 - j))
    #Calculating Scores
    scorepath = "/home/fuyilei96/ProteinAlignment/score_" + str(j) + "/"
    os.system("mkdir  " + scorepath)
    os.system("python score.py -af /home/fuyilei96/ProteinAlignment/proteinalignment/divided/sabre/output/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/ref/ -op " + scorepath + " -dbn sabre")
    os.system("python score.py -af /home/fuyilei96/ProteinAlignment/proteinalignment/divided/ox/output/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/ox/ref/ -op " + scorepath + " -dbn ox")
    os.system("python score.py -af /home/fuyilei96/ProteinAlignment/proteinalignment/divided/bali3/output/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/bali3/ref/ -op " + scorepath + " -dbn bali3")
    #Calculating Original Scores
    # os.system("python score.py -af /home/fuyilei96/ProteinAlignment/proteinalignment/divided/sabre/temp/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/ref/ -op /home/fuyilei96/ProteinAlignment/scores/ -dbn sabre_msaprobs")
    # os.system("python score.py -af /home/fuyilei96/ProteinAlignment/proteinalignment/divided/ox/temp/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/ox/ref/ -op /home/fuyilei96/ProteinAlignment/scores/ -dbn ox_msaprobs")
    # os.system("python score.py -af /home/fuyilei96/ProteinAlignment/proteinalignment/divided/bali3/temp/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/bali3/ref/ -op /home/fuyilei96/ProteinAlignment/scores/ -dbn bali3_msaprobs")
    os.system("rm -r /home/fuyilei96/ProteinAlignment/proteinalignment/divided/sabre /home/fuyilei96/ProteinAlignment/proteinalignment/divided/ox /home/fuyilei96/ProteinAlignment/proteinalignment/divided/bali3")
