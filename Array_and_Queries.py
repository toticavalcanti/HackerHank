# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 10:30:01 2018

@author: toti.cavalcanti
"""

#https://www.hackerrank.com/contests/hackerrank-hiring-contest/challenges/array-and-queries-1

def count_splits(A):
    A = sorted(A)
    count = 1
    max_n = 0
    repeat = False
    
    if len(A) == 2 and (A[0] == A[1] or abs(A[0] - A[1]) > 1):
        return 2
    elif len(A) == 1:
        return 1
    else:
        for i in range(len(A) - 1):
            #consecutivos e Repeat tá True
            if repeat == True and A[i + 1] - A[i] == 1:
                count = 2
                repeat = False
            #Consecutivos Repeat tá False
            elif A[i + 1] - A[i] == 1:
                count = 1
                repeat = False
            #Ou são iguais ou não consecutivos
            elif A[i + 1] - A[i] > 1 or A[i + 1] == A[i] and repeat == False:
                count += 1
                repeat = True
            elif A[i + 1] - A[i] > 1:
                count = max(A.count(A[i]), A.count(A[i + 1])) - 1
                repeat = False
            else:
                count = max(A.count(A[i]), A.count(A[i + 1]))
            if max_n < count:
                max_n = count
    return max_n      


#[2,2,2,1,1]
#[2,2,2,1,5]
#[1,2,3,4,3,5]
def arrayAndQueries(A, queries):
    # Complete this function
    result = 0
    for i, querie in enumerate(queries):
        A[querie[0] - 1] = querie[1]
        result += (count_splits(A) * (i + 1))
    return result
      

#assert(count([2, 2, 2, 1, 1])) == 3   

n = 5
A = [2, 2, 1, 1, 1]
q = 2
queries = [[3, 2], [5, 5]]

print(arrayAndQueries(A, queries))   


