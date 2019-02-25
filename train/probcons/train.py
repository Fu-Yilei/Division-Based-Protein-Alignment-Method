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

for i in range(15, 45, 5):
    for j in range(55, 85, 5):
        ff = str(float(i)/100)
        sf = str(float(j)/100)
        #delete remain files
        os.system("rm -r /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/probcons/sabre /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/probcons/ox /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/probcons/bali3")
        #mkdir
        os.system("mkdir  /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/probcons/sabre /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/probcons/ox /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/probcons/bali3")
        # print("python divide.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/in/ -ouf /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/probcons/sabre/ -ff " + ff + " -sf " + sf)
        os.system("python divide.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/in/ -ouf /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/probcons/sabre/ -ff " + ff + " -sf " + sf)
        os.system("python divide.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/ox/in/ -ouf /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/probcons/ox/ -ff " + ff + " -sf " + sf)
        os.system("python divide.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/bali3/in/ -ouf /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/probcons/bali3/ -ff " + ff + " -sf " + sf)

        #Calculating Scores
        scorepath = "/home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/probcons/scores_ff_" + ff +"_sf_" + sf + "/"
        os.system("mkdir " + scorepath)
        os.system("python score.py -af /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/probcons/sabre/output/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/ref/ -op " + scorepath + " -dbn sabre")
        os.system("python score.py -af /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/probcons/ox/output/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/ox/ref/ -op " + scorepath + " -dbn ox")
        os.system("python score.py -af /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/probcons/bali3/output/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/bali3/ref/ -op " + scorepath + " -dbn bali3")

            
#Calculating Original Scores
os.system("python score.py -af /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/probcons/sabre/temp/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/ref/ -op /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/probcons/scores_original/ -dbn sabre_probcons")
os.system("python score.py -af /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/probcons/ox/temp/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/ox/ref/ -op /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/probcons/scores_original/ -dbn ox_probcons")
os.system("python score.py -af /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/probcons/bali3/temp/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/bali3/ref/ -op /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/train/probcons/scores_original/ -dbn bali3_probcons")
