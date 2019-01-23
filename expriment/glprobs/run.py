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



os.system("mkdir  /home/fuyilei96/ProteinAlignment/proteinalignment/divided/sabre /home/fuyilei96/ProteinAlignment/proteinalignment/divided/ox /home/fuyilei96/ProteinAlignment/proteinalignment/divided/bali3")
os.system("python divide.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/in/ -ouf /home/fuyilei96/ProteinAlignment/proteinalignment/divided/sabre/")
os.system("python divide.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/ox/in/ -ouf /home/fuyilei96/ProteinAlignment/proteinalignment/divided/ox/ ")
os.system("python divide.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/bali3/in/ -ouf /home/fuyilei96/ProteinAlignment/proteinalignment/divided/bali3/ ")


#Calculating Scores
os.system("mkdir /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/expriment/glprobs/scores/")
os.system("python score.py -af /home/fuyilei96/ProteinAlignment/proteinalignment/divided/sabre/output/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/ref/ -op /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/expriment/glprobs/scores/ -dbn sabre")
os.system("python score.py -af /home/fuyilei96/ProteinAlignment/proteinalignment/divided/ox/output/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/ox/ref/ -op /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/expriment/glprobs/scores/ -dbn ox")
os.system("python score.py -af /home/fuyilei96/ProteinAlignment/proteinalignment/divided/bali3/output/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/bali3/ref/ -op /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/expriment/glprobs/scores/ -dbn bali3")
#Calculating Original Scores 
os.system("python score.py -af /home/fuyilei96/ProteinAlignment/proteinalignment/divided/sabre/temp/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/ref/ -op /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/expriment/glprobs/scores/ -dbn sabre_glprobs")
os.system("python score.py -af /home/fuyilei96/ProteinAlignment/proteinalignment/divided/ox/temp/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/ox/ref/ -op /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/expriment/glprobs/scores/ -dbn ox_glprobs")
os.system("python score.py -af /home/fuyilei96/ProteinAlignment/proteinalignment/divided/bali3/temp/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/bali3/ref/ -op /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/expriment/glprobs/scores/ -dbn bali3_glprobs")
#Delete useless files
os.system("rm -r /home/fuyilei96/ProteinAlignment/proteinalignment/divided/sabre /home/fuyilei96/ProteinAlignment/proteinalignment/divided/ox /home/fuyilei96/ProteinAlignment/proteinalignment/divided/bali3")
