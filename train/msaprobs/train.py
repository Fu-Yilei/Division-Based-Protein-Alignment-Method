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

for i in range(15, 20, 5):
    for j in range(70, 85, 5):
        ff = str(float(i)/100)
        sf = str(float(j)/100)
        #delete remain files
        os.system("rm -r /data3/fuyilei96/ProteinTest/msaprobs/sabre /data3/fuyilei96/ProteinTest/msaprobs/ox /data3/fuyilei96/ProteinTest/msaprobs/bali3")
        #mkdir
        os.system("mkdir  /data3/fuyilei96/ProteinTest/msaprobs/sabre /data3/fuyilei96/ProteinTest/msaprobs/ox /data3/fuyilei96/ProteinTest/msaprobs/bali3")
        os.system("mkdir /data3/fuyilei96/ProteinTest/msaprobs/sabre/" + "_ff_" + ff +"_sf_" + sf + "/" )
        os.system("mkdir /data3/fuyilei96/ProteinTest/msaprobs/ox/" + "_ff_" + ff +"_sf_" + sf + "/" )
        os.system("mkdir /data3/fuyilei96/ProteinTest/msaprobs/bali3/" + "_ff_" + ff +"_sf_" + sf + "/" )


        os.system("python divide.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/in/ -ouf /data3/fuyilei96/ProteinTest/msaprobs/sabre/" + "_ff_" + ff +"_sf_" + sf + "/" + " -ff " + ff + " -sf " + sf)
        os.system("python divide.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/ox/in/ -ouf /data3/fuyilei96/ProteinTest/msaprobs/ox/" + "_ff_" + ff +"_sf_" + sf + "/" + " -ff " + ff + " -sf " + sf)
        os.system("python divide.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/bali3/in/ -ouf /data3/fuyilei96/ProteinTest/msaprobs/bali3/" + "_ff_" + ff +"_sf_" + sf + "/" + " -ff " + ff + " -sf " + sf)

