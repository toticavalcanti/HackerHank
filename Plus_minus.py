#!/bin/python3

#https://www.hackerrank.com/challenges/plus-minus/problem

import sys

def plusMinus(arr):
    # Complete this function
    pos = sum([1 for i in arr if i > 0]) / len(arr)
    neg = sum([1 for i in arr if i < 0]) / len(arr)
    zero = sum([1 for i in arr if i == 0]) / len(arr)
    print("{:.6f}".format(pos))
    print("{:.6f}".format(neg))
    print("{:.6f}".format(zero))

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)

