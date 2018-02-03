# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 22:22:14 2018

@author: toti.cavalcanti
"""
#https://www.hackerrank.com/contests/hackerrank-hiring-contest/challenges/programming-competition/problem

# HackerRank has organized a hiring contest, from December until the end of January. The programmer who solves the most questions in this contest, will get an interview, which is the first step into getting hired in HackerRank. If multiple programmers have solved the highest number of questions (the case of a draw), the winner is the programmer with the maximum number of solved questions appearing first in the list as shown in the following example:

# image

# Given the number of programmers participating in the competition, their names and the number of questions they have solved from the beginning of December and until the end of January, find the name of the programmer who wins the competition and show how many questions he/she has solved during the competition.

# Input Format

# The first line contains an integer n denoting the number of programmers participating in the contest. 
# The following n lines contain a string namei, which represents the name of each programmer and two integers d and j, where, 
# d - number of questions the programmer has solved until the beginning of December. 
# j - number of questions the programmer has solved until the end of January.

# Constraints

# 3 <= n <= 1000
# 0 <= d <= j <= 200

# namei (the name of each programmer) can be composed of digits (0 - 9), lowercase (a - z) and uppercase (A - Z) characters, and it is a non-empty string with at most 10 characters
# The names of all programmers are unique
# Output Format

# Print the name of the programmer who will win the competition and the number of questions he/she has solved during the period of the competition.

# Sample Input 0

# 5
# Arber 5 11
# Ardit 4 12
# Marsed 3 5
# Gledi 2 2
# Ana 1 6
# Sample Output 0

# Ardit 8
# Explanation 0

# image

# Arber has solved 6 questions.
# Ardit has solved 8 questions.
# Marsed has solved 2 questions.
# Gledi has solved 0 questions.
# Ana has solved 5 questions.
# The winner is Ardit since he has solved most questions during contest time.

# Sample Input 1

# 5
# Arber 5 7
# Gledi 2 9
# Marsed 3 5
# Ardit 4 11
# Ana 1 6
# Sample Output 1

# Gledi 7
# Explanation 1


# Arber has solved 2 questions.
# Gledi has solved 7 questions.
# Marsed has solved 2 questions.
# Ardit has solved 7 questions.
# Ana has solved 5 questions.
# Gledi and Ardit have both solved 7 questions, but the winner is Gledi since he appears before Ardit in the list.

programmerList = ['Arber 5 11', 'Ardit 4 12', 'Marsed 3 5', 'Gledi 2 2', 'Ana 1 6']
list_out = []
pos_win = 0
maxi = 0
for programmer in programmerList:
    name, d, j = programmer.split(' ')
    list_out.append([str(name), int(d), int(j)])

for i in range(len(list_out)):
    if maxi < abs(list_out[i][2] - list_out[i][1]):
        maxi = abs(list_out[i][2] - list_out[i][1])
        pos_win = i
        
print(list_out[pos_win][0] + " " + str(maxi))

