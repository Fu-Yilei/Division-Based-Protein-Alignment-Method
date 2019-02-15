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



os.system("mkdir  /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/probcons/sabre /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/probcons/ox /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/probcons/bali3")
os.system("python divide.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/in/ -ouf /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/probcons/sabre/")
os.system("python divide.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/ox/in/ -ouf /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/probcons/ox/ ")
os.system("python divide.py -orf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/bali3/in/ -ouf /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/probcons/bali3/ ")
#Calculating Scores
os.system("mkdir /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/probcons/scores")
os.system("python score.py -af /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/probcons/sabre/output/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/ref/ -op /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/probcons/scores/ -dbn sabre")
os.system("python score.py -af /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/probcons/ox/output/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/ox/ref/ -op /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/probcons/scores/ -dbn ox")
os.system("python score.py -af /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/probcons/bali3/output/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/bali3/ref/ -op /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/probcons/scores/ -dbn bali3")
#Calculating Original Scores
os.system("python score.py -af /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/probcons/sabre/temp/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/sabre/ref/ -op /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/probcons/scores/ -dbn sabre_msaprobs")
os.system("python score.py -af /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/probcons/ox/temp/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/ox/ref/ -op /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/probcons/scores/ -dbn ox_msaprobs")
os.system("python score.py -af /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/probcons/bali3/temp/ -rf /home/fuyilei96/ProteinAlignment/proteinalignment/benchmark/bali3/ref/ -op /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/probcons/scores/ -dbn bali3_msaprobs")
# os.system("rm -r /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/probcons/sabre /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/probcons/ox /home/fuyilei96/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/probcons/bali3")
