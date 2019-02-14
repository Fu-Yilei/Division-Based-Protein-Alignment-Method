#!/usr/bin/env python

''' 
 * All rights Reserved, Designed By HIT-Bioinformatics   
 * @Title:  run.py
 * @Description: Run program for probalign program.
 * @author: fuyilei96
 * @date: December 21 2018
 * @version V3.0.0   
'''


import sys
import argparse
import os



os.system("mkdir  home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/expriment/probalign/sabre home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/expriment/probalign/ox home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/expriment/probalign/bali3")
os.system("python divide.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/in/ -ouf home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/expriment/probalign/sabre/")
os.system("python divide.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/ox/in/ -ouf home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/expriment/probalign/ox/ ")
os.system("python divide.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/bali3/in/ -ouf home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/expriment/probalign/bali3/ ")
#Calculating Scores
os.system("mkdir /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/expriment/probalign/scores")
os.system("python score.py -af home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/expriment/probalign/sabre/output/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/ref/ -op /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/expriment/probalign/scores/ -dbn sabre")
os.system("python score.py -af home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/expriment/probalign/ox/output/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/ox/ref/ -op /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/expriment/probalign/scores/ -dbn ox")
os.system("python score.py -af home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/expriment/probalign/bali3/output/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/bali3/ref/ -op /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/expriment/probalign/scores/ -dbn bali3")
#Calculating Original Scores
os.system("python score.py -af home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/expriment/probalign/sabre/temp/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/ref/ -op /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/expriment/probalign/scores/ -dbn sabre_probalign")
os.system("python score.py -af home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/expriment/probalign/ox/temp/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/ox/ref/ -op /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/expriment/probalign/scores/ -dbn ox_probalign")
os.system("python score.py -af home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/expriment/probalign/bali3/temp/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/bali3/ref/ -op /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/expriment/probalign/scores/ -dbn bali3_probalign")
# os.system("rm -r home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/expriment/probalign/sabre home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/expriment/probalign/ox home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/expriment/probalign/bali3")
