# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 12:07:33 2018

@author: toti.cavalcanti
"""

#!/bin/python3

import sys

def diagonalDifference(a):
    # Complete this function
    diagonal_left_to_right = 0
    diagonal_right_to_left = 0
    
    for i in range(n):
        diagonal_left_to_right += a[i][i]
        
    for i in range(n):
        diagonal_right_to_left += list(reversed(a[i]))[i]
        
    return(abs(diagonal_left_to_right - diagonal_right_to_left))
if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)
