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
for i in range(100, 400, 100):
    os.system("rm -r /data3/fuyilei96/ProteinTest/probcons/sabre/refinement /data3/fuyilei96/ProteinTest/probcons/ox/refinement /data3/fuyilei96/ProteinTest/probcons/bali3/refinement")
    # #mkdir
    os.system("mkdir  /data3/fuyilei96/ProteinTest/probcons/sabre /data3/fuyilei96/ProteinTest/probcons/ox /data3/fuyilei96/ProteinTest/probcons/bali3")
    os.system("mkdir /data3/fuyilei96/ProteinTest/probcons/sabre/refinement" )
    os.system("mkdir /data3/fuyilei96/ProteinTest/probcons/ox/refinement" )
    os.system("mkdir /data3/fuyilei96/ProteinTest/probcons/bali3/refinement" )


    os.system("python refinement.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/in/ -ouf /data3/fuyilei96/ProteinTest/probcons/sabre/ -rt " + str(i))
    os.system("python refinement.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/ox/in/ -ouf /data3/fuyilei96/ProteinTest/probcons/ox/ -rt " + str(i))
    os.system("python refinement.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/bali3/in/ -ouf /data3/fuyilei96/ProteinTest/probcons/bali3/ -rt " + str(i))

    #Calculating Scores
    
    # scorepath = "/data3/fuyilei96/ProteinTest/probcons/"
    scorepath = "/data3/fuyilei96/ProteinTest/probcons/refinement/"+str(i)+"/"
    os.system("mkdir /data3/fuyilei96/ProteinTest/probcons/refinement/")
    os.system("mkdir " + scorepath)
    os.system("python score.py -af /data3/fuyilei96/ProteinTest/probcons/sabre/refinement/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/ref/ -op " + scorepath + " -dbn sabre")
    os.system("python score.py -af /data3/fuyilei96/ProteinTest/probcons/ox/refinement/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/ox/ref/ -op " + scorepath + " -dbn ox")
    os.system("python score.py -af /data3/fuyilei96/ProteinTest/probcons/bali3/refinement/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/bali3/ref/ -op " + scorepath + " -dbn bali3")

