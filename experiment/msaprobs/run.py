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



# os.system("mkdir  /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/msaprobs/sabre /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/msaprobs/ox /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/msaprobs/bali3")
# os.system("python divide.py -orf /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/proteinalignment/benchmark/sabre/in/ -ouf /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/msaprobs/sabre/")
# os.system("python divide.py -orf /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/proteinalignment/benchmark/ox/in/ -ouf /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/msaprobs/ox/ ")
# os.system("python divide.py -orf /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/proteinalignment/benchmark/bali3/in/ -ouf /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/msaprobs/bali3/ ")

#Calculating Scores
os.system("mkdir /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/msaprobs/scores/")
os.system("python score.py -af /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/msaprobs/sabre/output/ -rf /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/proteinalignment/benchmark/sabre/ref/ -op /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/msaprobs/scores/ -dbn sabre")
os.system("python score.py -af /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/msaprobs/ox/output/ -rf /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/proteinalignment/benchmark/ox/ref/ -op /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/msaprobs/scores/ -dbn ox")
os.system("python score.py -af /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/msaprobs/bali3/output/ -rf /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/proteinalignment/benchmark/bali3/ref/ -op /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/msaprobs/scores/ -dbn bali3")

#Calculating Original Scores
os.system("python score.py -af /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/msaprobs/sabre/temp/ -rf /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/proteinalignment/benchmark/sabre/ref/ -op /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/msaprobs/scores/ -dbn sabre_msaprobs")
os.system("python score.py -af /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/msaprobs/ox/temp/ -rf /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/proteinalignment/benchmark/ox/ref/ -op /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/msaprobs/scores/ -dbn ox_msaprobs")
os.system("python score.py -af /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/msaprobs/bali3/temp/ -rf /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/proteinalignment/benchmark/bali3/ref/ -op /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/msaprobs/scores/ -dbn bali3_msaprobs")
# os.system("rm -r /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/msaprobs/sabre /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/msaprobs/ox /mnt/c/Users/fuyil/OneDrive/bioinformatics/Protein/ProteinAlignment/Division-Based-Protein-Alignment-Method/experiment/msaprobs/bali3")
