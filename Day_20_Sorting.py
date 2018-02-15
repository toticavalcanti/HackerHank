#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
numberOfSwaps = 0;
# Write Your Code Here
for i in range(n):
    #Track number of elements swapped during a single array traversal 
    for j in range(n - 1):
        #Swap adjacent elements if they are in decreasing order
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            numberOfSwaps += 1
    


print("Array is sorted in " + str(numberOfSwaps) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[n - 1]))
          