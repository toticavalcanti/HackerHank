#!/bin/python3

import sys

def factorial(n):
    # Complete this function
    if n == 0 or n == 1:
        return 1
    else:
        return(factorial(n - 1) * n)
    
if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)