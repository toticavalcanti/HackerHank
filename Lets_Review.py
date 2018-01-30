#!/bin/python3

import sys

if __name__ == '__main__':
    lines = []
    # Reading the first line and converting it to an integer
    N = int(input())
    # Running a for loop to read each of the following lines
    for i in range(N):
        current_line = input()
        lines.append(current_line)
    
    for line in lines:
        space = ' '
        output_even = []
        output_odd = []
        for i, c in enumerate(line):
            if i % 2 == 0:
                output_even.append(c)
            else:
                output_odd.append(c)
        
        str_even = ''.join(output_even)
        str_odd = ''.join(output_odd)
        print(str_even + space + str_odd)