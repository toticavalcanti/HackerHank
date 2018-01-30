# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 17:56:07 2018

@author: toti.cavalcanti
"""

import sys

def decToBin(n):
    b = ''
    while n != 0:
        b = b + str(n % 2)
        n = int(n / 2)
    return b[::-1]
    
#n = int(input().strip())
n = 524275

binary = decToBin(n)

max_consec = 0  

max_temp = 0

for bit in binary:
    if bit == '1':
        max_temp += 1
        if max_consec < max_temp:
            max_consec = max_temp
    else:
         if max_consec < max_temp:
             max_consec = max_temp
         max_temp = 0
        
print(max_consec)
