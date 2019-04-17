#!/usr/bin/env python

'''
 * All rights Reserved, Designed By HIT-Bioinformatics   
 * @Title:  run.py
 * @Description: Run program
 * @author: fuyilei96
 * @date: December 21 2018
 * @version V2.0.0   
'''


import sys
import os
for i in range(10, 40, 10):
    #mkdir
    os.system("mkdir  /data3/fuyilei96/ProteinTest/msaprobs/sabre /data3/fuyilei96/ProteinTest/msaprobs/ox /data3/fuyilei96/ProteinTest/msaprobs/bali3")
    os.system("mkdir /data3/fuyilei96/ProteinTest/msaprobs/sabre/refinement" )
    os.system("mkdir /data3/fuyilei96/ProteinTest/msaprobs/ox/refinement" )
    os.system("mkdir /data3/fuyilei96/ProteinTest/msaprobs/bali3/refinement" )


    os.system("python refinement.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/in/ -ouf /data3/fuyilei96/ProteinTest/msaprobs/sabre/ -rt " + str(i) )
    os.system("python refinement.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/ox/in/ -ouf /data3/fuyilei96/ProteinTest/msaprobs/ox/ -rt " + str(i)  )
    os.system("python refinement.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/bali3/in/ -ouf /data3/fuyilei96/ProteinTest/msaprobs/bali3/ -rt " + str(i)  )

    #Calculating Scores
    scorepath = "/data3/fuyilei96/ProteinTest/msaprobs/refinement/"+str(i)+"/"
    os.system("mkdir /data3/fuyilei96/ProteinTest/msaprobs/refinement/")
    os.system("mkdir " + scorepath)
    os.system("python score_8.py -af /data3/fuyilei96/ProteinTest/msaprobs/sabre/refinement/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/ref/ -op " + scorepath + " -dbn sabre")
    os.system("python score_8.py -af /data3/fuyilei96/ProteinTest/msaprobs/ox/refinement/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/ox/ref/ -op " + scorepath + " -dbn ox")
    os.system("python score_8.py -af /data3/fuyilei96/ProteinTest/msaprobs/bali3/refinement/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/bali3/ref/ -op " + scorepath + " -dbn bali3")

