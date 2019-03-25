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
        os.system("rm -r /data3/fuyilei96/Division-Based-Protein-Alignment-Method/train/probalign/sabre /data3/fuyilei96/Division-Based-Protein-Alignment-Method/train/probalign/ox /data3/fuyilei96/Division-Based-Protein-Alignment-Method/train/probalign/bali3")
        #mkdir
        os.system("mkdir  /data3/fuyilei96/Division-Based-Protein-Alignment-Method/train/probalign/sabre /data3/fuyilei96/Division-Based-Protein-Alignment-Method/train/probalign/ox /data3/fuyilei96/Division-Based-Protein-Alignment-Method/train/probalign/bali3")
        os.system("mkdir /data3/fuyilei96/Division-Based-Protein-Alignment-Method/train/probalign/sabre/" + "_ff_" + ff +"_sf_" + sf + "/" )
        os.system("mkdir /data3/fuyilei96/Division-Based-Protein-Alignment-Method/train/probalign/ox/" + "_ff_" + ff +"_sf_" + sf + "/" )
        os.system("mkdir /data3/fuyilei96/Division-Based-Protein-Alignment-Method/train/probalign/bali3/" + "_ff_" + ff +"_sf_" + sf + "/" )


        os.system("python divide.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/in/ -ouf /data3/fuyilei96/Division-Based-Protein-Alignment-Method/train/probalign/sabre/" + "_ff_" + ff +"_sf_" + sf + "/" + " -ff " + ff + " -sf " + sf)
        os.system("python divide.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/ox/in/ -ouf /data3/fuyilei96/Division-Based-Protein-Alignment-Method/train/probalign/ox/" + "_ff_" + ff +"_sf_" + sf + "/" + " -ff " + ff + " -sf " + sf)
        os.system("python divide.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/bali3/in/ -ouf /data3/fuyilei96/Division-Based-Protein-Alignment-Method/train/probalign/bali3/" + "_ff_" + ff +"_sf_" + sf + "/" + " -ff " + ff + " -sf " + sf)

#         #Calculating Scores
#         scorepath = "/data3/fuyilei96/Division-Based-Protein-Alignment-Method/train/probalign/scores_ff_" + ff +"_sf_" + sf + "/"
#         os.system("mkdir " + scorepath)
#         os.system("python score.py -af /data3/fuyilei96/Division-Based-Protein-Alignment-Method/train/probalign/sabre/output/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/ref/ -op " + scorepath + " -dbn sabre")
#         os.system("python score.py -af /data3/fuyilei96/Division-Based-Protein-Alignment-Method/train/probalign/ox/output/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/ox/ref/ -op " + scorepath + " -dbn ox")
#         os.system("python score.py -af /data3/fuyilei96/Division-Based-Protein-Alignment-Method/train/probalign/bali3/output/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/bali3/ref/ -op " + scorepath + " -dbn bali3")

            
# #Calculating Original Scores
# os.system("python score.py -af /data3/fuyilei96/Division-Based-Protein-Alignment-Method/train/probalign/sabre/temp/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/ref/ -op /data3/fuyilei96/Division-Based-Protein-Alignment-Method/train/probalign/scores_original/ -dbn sabre_probalign")
# os.system("python score.py -af /data3/fuyilei96/Division-Based-Protein-Alignment-Method/train/probalign/ox/temp/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/ox/ref/ -op /data3/fuyilei96/Division-Based-Protein-Alignment-Method/train/probalign/scores_original/ -dbn ox_probalign")
# os.system("python score.py -af /data3/fuyilei96/Division-Based-Protein-Alignment-Method/train/probalign/bali3/temp/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/bali3/ref/ -op /data3/fuyilei96/Division-Based-Protein-Alignment-Method/train/probalign/scores_original/ -dbn bali3_probalign")
