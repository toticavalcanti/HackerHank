# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 10:01:57 2018

@author: toti.cavalcanti
"""

#https://www.hackerrank.com/challenges/30-2d-arrays/problem

#!/bin/python3

import sys

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

#because the hourglass has 7 possible values and the minimal value possible is -9
sum_max = -9 * 7

for row in range(len(arr) - 2):
	for column in range(len(arr[row]) - 2):
        #part of up hourglass
		up_hourglass_1 = arr[row][column]
		up_hourglass_2 = arr[row][column + 1]
		up_hourglass_3 = arr[row][column + 2]
        #part of middle hourglass
		middle_hourglass = arr[row + 1][column + 1]
        #part of down hourglass
		down_hourglass_1 = arr[row + 2][column]
		down_hourglass_2 = arr[row + 2][column + 1]
		down_hourglass_3 = arr[row + 2][column + 2]
        #sum each hourglass
		su = up_hourglass_1 + up_hourglass_2 + up_hourglass_3 + middle_hourglass + down_hourglass_1 + down_hourglass_2 + down_hourglass_3
		sum_max = max(su, sum_max)

print(sum_max)
