# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 16:28:48 2018

@author: toti.cavalcanti
"""

#!/bin/python3

import sys

def miniMaxSum(arr):
    # Complete this function
    arr.sort()
    print("{} {}".format(sum(arr[0:len(arr) - 1]), sum(arr[1:len(arr)])))
    

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)

