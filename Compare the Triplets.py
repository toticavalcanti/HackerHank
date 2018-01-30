# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 18:25:13 2018

@author: toti.cavalcanti
"""

def solve(a0, a1, a2, b0, b1, b2):
    alice_points = 0
    bob_points = 0
    # Complete this function
    if a0 > b0:
        alice_points += 1
    elif a0 < b0: 
        bob_points += 1
    
    if a1 > b1:
        alice_points += 1
    elif a1 < b1: 
        bob_points += 1
        
    if a2 > b2:
        alice_points += 1
    elif a2 < b2: 
        bob_points += 1
        
        return ([alice_points, bob_points])
    
res = solve(1,2,3,1,2,3)

res

