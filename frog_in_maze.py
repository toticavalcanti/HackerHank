# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 16:28:48 2018

@author: toti.cavalcanti
"""

#!/bin/python3

import sys

def find_A_position(mat):
    for n, line in enumerate(mat):
        if 'A' in line:
            return [n, line.index('A')]

n, m, k = input().strip().split(' ')	
n, m, k = [int(n), int(m), int(k)]
mat = []
for a0 in range(n):
    mat.append(list(input().strip()))

pos_A = find_A_position(mat)

#pos_m_a = index.mat[pos_n_A]('A')
print(pos_A)
        
    

#for i in range(n):
#    for j in range(m):
#        
##[['#', '#', '#', '*', 'O', 'O'], 
## ['O', '#', 'O', 'A', '%', 'O'], 
## ['#', '#', '#', '*', 'O', 'O']]
#
#    
#    # Write Your Code Here
#    
#for a0 in range(k):
#    i1, j1, i2, j2 = input().strip().split(' ')
#    # coordinates of both entrances of the tunnel
#    i1, j1, i2, j2 = [int(i1), int(j1), int(i2), int(j2)]
#    
    # Write Your Code Here
# Write Your Code Here