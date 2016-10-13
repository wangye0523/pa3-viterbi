#!/usr/lib/env python
#-*- coding=utf-8 -*-

import sys
import os
import re
import pprint
import math

default_tag = ['prep', 'noun', 'verb', 'inf', 'phi', 'fin']


def Probabilities_file(file):
    tag_dict = {}
    prob_dict = {}


    raw_mat=[]
    with open (file,'r') as f:
        for ff in f:
            raw_mat.append(ff)
            test=ff.split()
            if test[0] in default_tag:
                tag_dict[test[0],test[1]]= test[2]
            else:
                prob_dict[test[0],test[1]]= test[2]
    return tag_dict,prob_dict


tag_dict,prob_dict = Probabilities_file('probs.txt')

testwords='mark has fish'
testwords=testwords.split()


total_iteration=len(testwords)+1

i=0
pi={}
v=[]
for t in testwords:
    for tt in default_tag:
        keyword=(t,tt)
        # keyword=str(keyword)
        prob_dict[keyword]=prob_dict.get(keyword, '0.0001')

for tt in default_tag:
    for ttt in default_tag:
        key_keyword=(tt,ttt)
        tag_dict[key_keyword]=tag_dict.get(key_keyword,'0.0001')



##default the pi[]
for k in range(1,len(testwords)+3):
    for tag in default_tag:
        pi[k-1,tag] = prob_dict.get((k-1,tag),0.0001)

# i=0
# pi[0,]
# for k in range(1,len(testwords)+1):
#     for tag_test in default_tag:
#         qqq=tag_dict[]


# def main(probabilities_path, sentences_path):
#
#     guess_list = process_dir(data_path)
#     gold_list =  get_gold(gold_path)
#     score(guess_list, gold_list)
#
#
#
# if __name__ == '__main__':
#     if (len(sys.argv) != 3):
#         print 'usage:\tviterbi.py <probabilities file> <sentences file>'
#         sys.exit(0)
#     main(sys.argv[1],sys.argv[2])


