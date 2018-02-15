i = 4
d = 4.0
s = 'HackerRank '

import sys
# Declare second integer, double, and String variables.
entradas = []
for line in sys.stdin:
    entradas.append(line)
# Read and save an integer, double, and String to your variables.
a = entradas[0]
b = entradas[1]
c = entradas[2]

# Print the sum of both integer variables on a new line.
print(int(a) + i)
# Print the sum of the double variables on a new line.
print(float(b) + d)
# Concatenate and print the String variables on a new line
print(s + c)
# The 's' variable above should be printed first.