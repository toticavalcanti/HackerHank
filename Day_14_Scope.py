# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 15:51:47 2018

@author: toti.cavalcanti
"""

#https://www.hackerrank.com/challenges/30-scope/problem

class Difference:
    def __init__(self, a):
        self.__elements = a
    # Add your code here
    def computeDifference(self):
        max_diff = 0
        for i in range(len(self.__elements)):
            for j in range(len(self.__elements)):
                val_abs = abs(self.__elements[i] - self.__elements[j])
                if val_abs > max_diff:
                    max_diff = val_abs

        self.maximumDifference = max_diff
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)