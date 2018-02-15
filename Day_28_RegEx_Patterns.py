# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 15:10:31 2018

@author: toti.cavalcanti
"""

#!/bin/python3

import re

lst = []
N = int(input().strip())
for a0 in range(N):
    firstName, emailID = input().strip().split(' ')
    firstName, emailID = [str(firstName),str(emailID)]
    
    if re.search(r'[a-z]@gmail.com', emailID):
        lst.append(firstName)

lst.sort()
for name in lst:
    print(name)


