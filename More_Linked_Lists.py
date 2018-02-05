
#https://www.hackerrank.com/challenges/30-linked-list-deletion/problem
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
        
class Solution: 
    def insert(self, head, data):
            p = Node(data)           
            if head == None:
                head = p
            elif head.next == None:
                head.next = p
            else:
                start = head
                while(start.next != None):
                    start = start.next
                start.next = p
            return head  
        
    def display(self, head):
        current = head
        while current:
            print(current.data, end=" ")
            current = current.next
    
    
    def removeDuplicates(self, head):
        current = head
        while current is not None and current.next is not None:
            while current.next is not None and current.data is current.next.data:
                current.next = current.next.next
            current = current.next
        return head
        
        
mylist = Solution()
T = 6#int(input())
head = None
dados = [1,2,2,3,3,4]
for i in range(T):
    data = dados[i]#int(input())
    head = mylist.insert(head, data)
head = mylist.removeDuplicates(head)
mylist.display(head)