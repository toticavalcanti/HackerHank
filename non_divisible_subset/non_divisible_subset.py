#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    total = 0
    mods = [0] * k
    for n in s:
        mods[n % k] += 1
    #can only have 1 value congruent to 0 mod k
    total += min(1, mods[0])
    # if even, can only have 1 value congruent to k/2 mod k
    if (k % 2 == 0):
        total += min(1, mods[k // 2])
    # for all others, pick max of those k and n-k mod k
    for i in range(1, (k + 1) // 2):
        total += max(mods[i], mods[k - i])
    return total

if __name__ == '__main__':

    while True:
        try:
            first_multiple_input = input().rstrip().split()

            n = int(first_multiple_input[0])

            k = int(first_multiple_input[1])

            s = list(map(int, input().rstrip().split()))

            result = nonDivisibleSubset(k, s)
            print(result)

        except(EOFError):
            break