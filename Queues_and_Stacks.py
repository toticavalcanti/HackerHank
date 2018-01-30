# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 15:56:48 2018

@author: toti.cavalcanti
"""
#https://www.hackerrank.com/challenges/30-queues-stacks/problem

class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []

    def popCharacter(self):
        return self.stack.pop()

    def pushCharacter(self, ch):
        self.stack.append(ch)

    def dequeueCharacter(self):
        ch = self.queue[0]
        self.queue = self.queue[1:]
        return ch

    def enqueueCharacter(self, ch):
        self.queue.append(ch)


# read the string s
#s = input()
# Create the Solution class object

s = "arara"
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
print(obj.stack)
print(obj.queue)

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")