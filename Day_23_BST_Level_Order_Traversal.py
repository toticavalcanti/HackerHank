# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:36:43 2018

@author: toti.cavalcanti
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:31:44 2018

@author: toti.cavalcanti
"""
import sys

class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data
class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root
    
    def levelOrder(self, root):
        queue = [root]
        while len(queue) is not 0:
            current = queue[0]
            queue = queue[1:]
            print(str(current.data) + " ", end="")

            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
    
myTree.levelOrder(root)
