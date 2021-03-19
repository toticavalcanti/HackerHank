#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the longestCommonSubsequence function below.
def lcs(X , Y): 
    # length of the strings 
    m = len(X) #rows
    n = len(Y) #cols
    # array for storing the dinamic programing values 
    L = [[None] * (n + 1) for i in range(m + 1)] 
  
    """Following steps build L[m + 1][n + 1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i - 1] 
    and Y[0..j - 1]"""
    for i in range(m + 1): 
        for j in range(n + 1): 
            #base case
            if i == 0 or j == 0 : 
                L[i][j] = 0
            #
            elif X[i - 1] == Y[j - 1]: 
                L[i][j] = L[i - 1][j - 1] + 1
            else: 
                L[i][j] = max(L[i - 1][j] , L[i][j - 1])
  
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
    return L[m][n] 

#m = 5
#n = 6
#Range: i => 0 to 6
#Range: j => 0 to 7
#end of function lcs 

#X = [1, 2, 3, 4, 1]
#Y = [3, 4, 1, 2, 1, 3]

#L matrix final
#   j = columns
#i  0  1  2  3  4  5  6
#0 [0, 0, 0, 0, 0, 0, 0], 
#1 [0, 0, 0, 1, 1, 1, 1], 
#2 [0, 0, 0, 1, 2, 2, 2], 
#3 [0, 1, 1, 1, 2, 2, 3], 
#4 [0, 1, 2, 2, 2, 2, 3], 
#5 [0, 1, 2, 3, 3, 3, 3]

if __name__ == '__main__':

    n, m = input().split()

    n = int(n)

    m = int(n)

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))
    print(a)
    print(b)
    print('O tamanho da maior subsequência comum é: ' + str(lcs(a, b)))

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
    