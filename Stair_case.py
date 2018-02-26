#!/bin/python3

#https://www.hackerrank.com/challenges/staircase/problem

import sys

def staircase(n):
    spaces = n - 1
    for i in range(n):
        print(" " * spaces + "#" * (i + 1))
        spaces -= 1

if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)
