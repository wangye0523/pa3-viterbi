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


for ii in prob_dict:
    prob_dict[ii]=math.log(float(prob_dict[ii]))

for iii in pi:
    pi[iii]=math.log(float(pi[iii]))

for iiii in tag_dict:
    tag_dict[iiii]=math.log(float(tag_dict[iiii]))




MIN_FLOAT = -3.14e100
MIN_INF = float("-inf")

if sys.version_info[0] > 2:
    xrange = range


def get_top_states(t_state_v, K=4):
    return sorted(t_state_v, key=t_state_v.__getitem__, reverse=True)[:K]

obs=testwords
states=default_tag
start_p={(0, 'fin') = -9.21034037198
(0, 'inf') =  -9.21034037198
(0, 'noun')=  -9.21034037198
(0, 'phi')= -9.21034037198
(0, 'prep') = -9.21034037198
(0, 'verb') = -9.21034037198
}

trans_p=tag_dict
emit_p=prob_dict
def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]  # tabular
    mem_path = [{}]
    all_states = trans_p.keys()
    for y in states.get(obs[0], all_states):  # init
        V[0][y] = start_p[y] + emit_p[y].get(obs[0], MIN_FLOAT)
        mem_path[0][y] = ''
    for t in xrange(1, len(obs)):
        V.append({})
        mem_path.append({})
        #prev_states = get_top_states(V[t-1])
        prev_states = [
            x for x in mem_path[t - 1].keys() if len(trans_p[x]) > 0]

        prev_states_expect_next = set(
            (y for x in prev_states for y in trans_p[x].keys()))
        obs_states = set(
            states.get(obs[t], all_states)) & prev_states_expect_next

        if not obs_states:
            obs_states = prev_states_expect_next if prev_states_expect_next else all_states

        for y in obs_states:
            prob, state = max((V[t - 1][y0] + trans_p[y0].get(y, MIN_INF) +
                               emit_p[y].get(obs[t], MIN_FLOAT), y0) for y0 in prev_states)
            V[t][y] = prob
            mem_path[t][y] = state

    last = [(V[-1][y], y) for y in mem_path[-1].keys()]
    # if len(last)==0:
    #     print obs
    prob, state = max(last)

    route = [None] * len(obs)
    i = len(obs) - 1
    while i >= 0:
        route[i] = state
        state = mem_path[i][state]
        i -= 1
    return (prob, route)





exit()
i=0
for k in range(1,len(testwords)+1):
    for tag_test in default_tag:
        tmp=[0.0001]
        for previous_state in default_tag:
            qqq=tag_dict[tag,previous_state]
            tmp.append(pi[k-1,tag_test])

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


