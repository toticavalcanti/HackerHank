#!/bin/python3

import sys

def func(N):
    if N % 2 != 0:
        print('Weird')
    elif N % 2 == 0 and N < 5:
        print('Not Weird')
    elif N % 2 == 0 and N <= 20:
        print('Weird')
    elif N > 20:
        print('Not Weird')

N = int(input().strip())

func(N)