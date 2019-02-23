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
import argparse
import os


for i in range(15, 45, 5):
    for j in range(85, 55, 5):
        ff = str(float(i)/100)
        sf = str(float(j)/100)
        #delete remain files
        os.system("rm -r /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/msaprobs/sabre /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/msaprobs/ox /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/msaprobs/bali3")
        #mkdir
        os.system("mkdir  /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/msaprobs/sabre /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/msaprobs/ox /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/msaprobs/bali3")
        print("python divide.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/in/ -ouf /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/msaprobs/sabre/ -ff " + ff + " -sf " + sf)
        os.system("python divide.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/in/ -ouf /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/msaprobs/sabre/ -ff " + ff + " -sf " + sf)
        os.system("python divide.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/ox/in/ -ouf /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/msaprobs/ox/ -ff " + ff + " -sf " + sf)
        os.system("python divide.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/bali3/in/ -ouf /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/msaprobs/bali3/ -ff " + ff + " -sf " + sf)

        #Calculating Scores
        scorepath = "/home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/msaprobs/score_ff_" + ff +"_sf_" + sf + "/"
        os.system("mkdir " + scorepath)
        os.system("python score.py -af /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/msaprobs/sabre/output/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/ref/ -op " + scorepath + " -dbn sabre")
        os.system("python score.py -af /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/msaprobs/ox/output/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/ox/ref/ -op " + scorepath + " -dbn ox")
        os.system("python score.py -af /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/msaprobs/bali3/output/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/bali3/ref/ -op " + scorepath + " -dbn bali3")

       
#Calculating Original Scores
os.system("python score.py -af /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/msaprobs/sabre/temp/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/ref/ -op /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/msaprobs/scores_original/ -dbn sabre_msaprobs")
os.system("python score.py -af /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/msaprobs/ox/temp/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/ox/ref/ -op /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/msaprobs/scores_original/ -dbn ox_msaprobs")
os.system("python score.py -af /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/msaprobs/bali3/temp/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/bali3/ref/ -op /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/msaprobs/scores_original/ -dbn bali3_msaprobs")
