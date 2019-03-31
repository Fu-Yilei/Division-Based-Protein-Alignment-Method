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
    for j in range(55, 95, 5):
        ff = str(i/100.0)
        sf = str(j/100.0)

        #Calculating Scores
        scorepath = "/data3/fuyilei96/Division-Based-Protein-Alignment-Method/train/msaprobs/scores_ff_" + ff +"_sf_" + sf + "/"
        os.system("mkdir " + scorepath)
        os.system("python score_8.py -af /data3/fuyilei96/ProteinTest/msaprobs/sabre/" + "_ff_" + ff +"_sf_" + sf + "/output/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/ref/ -op " + scorepath + " -dbn sabre")
        os.system("python score_8.py -af /data3/fuyilei96/ProteinTest/msaprobs/ox/" + "_ff_" + ff +"_sf_" + sf + "/output/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/ox/ref/ -op " + scorepath + " -dbn ox")
        os.system("python score_8.py -af /data3/fuyilei96/ProteinTest/msaprobs/bali3/" + "_ff_" + ff +"_sf_" + sf + "/output/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/bali3/ref/ -op " + scorepath + " -dbn bali3")

            
# #Calculating Original Scores
# os.system("python score_8.py -af /data3/fuyilei96/Division-Based-Protein-Alignment-Method/train/msaprobs/sabre/temp/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/ref/ -op /data3/fuyilei96/Division-Based-Protein-Alignment-Method/train/msaprobs/scores_original/ -dbn sabre_msaprobs")
# os.system("python score_8.py -af /data3/fuyilei96/Division-Based-Protein-Alignment-Method/train/msaprobs/ox/temp/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/ox/ref/ -op /data3/fuyilei96/Division-Based-Protein-Alignment-Method/train/msaprobs/scores_original/ -dbn ox_msaprobs")
# os.system("python score_8.py -af /data3/fuyilei96/Division-Based-Protein-Alignment-Method/train/msaprobs/bali3/temp/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/bali3/ref/ -op /data3/fuyilei96/Division-Based-Protein-Alignment-Method/train/msaprobs/scores_original/ -dbn bali3_msaprobs")
