# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:48:41 2018

@author: toti.cavalcanti
"""
#https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem

import sys


S = input().strip()

try:
    num = int(S)
    print(S)
except ValueError:
    print('Bad String')