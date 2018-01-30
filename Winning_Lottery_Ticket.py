# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 17:11:20 2018

@author: toti.cavalcanti
"""

#https://www.hackerrank.com/contests/hackerrank-hiring-contest/challenges/winning-lottery-ticket

def sum_list_values(list01, list02):
    gab = [0] * 10
    for num in range(10):
        gab[num] += list01[num] + list02[num]
    return gab
    
def fill_gabs(tickets):
    gabs = []
    for i in range(len(tickets)):
        gab = [0] * 10
        for j in range(0, len(tickets[i])):
            gab[int(tickets[i][j])] += 1
        gabs.append(gab)
    return gabs

def winningLotteryTicket(tickets):
    # Complete this function
    count = 0
    gabs = fill_gabs(tickets)
    for i in range(len(gabs)):
        for j in range(i + 1, len(gabs)):
            gab = sum_list_values(gabs[i], gabs[j])
            if 0 not in gab:
                count += 1
    return count

#ent = ['129300455', '5559948277', '012334556', '56789', '123456879']

ent = ['0123456789', '1023456789', '129300455', '12930045', '129304550','5559948277', '012334556', '56789', '5678955', '123456879' ]
print(winningLotteryTicket(ent))

#gabs = [
#        [2, 1, 1, 1, 1, 2, 0, 0, 0, 1], 
#        [0, 0, 1, 0, 1, 3, 0, 2, 1, 2], 
#        [1, 1, 1, 2, 1, 2, 1, 0, 0, 0], 
#        [0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 
#        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#        
#        ]