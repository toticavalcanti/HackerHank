# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 15:07:41 2018

@author: toti.cavalcanti
"""
#https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem
from math import sqrt

T = int(input())

def isPrime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i is 0:
            return False
    return True


for _ in range(T):
    num = int(input())
    print("Prime") if num >= 2 and isPrime(num) else print("Not prime")