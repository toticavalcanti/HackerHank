#!/bin/python3

import sys
from math import ceil, floor
        
T = int(input().strip())

def chan(r,N):
    val = 0.5*(N**2 - (N % r)*ceil(N/r)**2 - (r - (N % r))*floor(N/r)**2)
    return(val)
    

def binS(M,N):
    r = N
    search = True
    lower_bound = 0
    upper_bound = N
    while search:
        if chan(r-1,N) < M and chan(r,N) >= M:
            search = False
            break
        if chan(r,N) < M and chan(r+1,N) >= M:
            search = False
            r=r+1
            break
        if M < chan(r,N):
            if r < upper_bound:
                upper_bound = r
        else:
            if r > lower_bound:
                lower_bound = r
        r = round((upper_bound+lower_bound)/2)
    return(r)

print(binS(3, 2))

   
for i in range(T):
   N,M = [int(q_temp) for q_temp in input().strip().split(' ')]
   val = binS(M,N)
   print(val)