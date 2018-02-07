# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:34:39 2018

@author: toti.cavalcanti
"""

act = str(input()).split(" ")
day_act = int(act[0])
month_act = int(act[1])
year_act = int(act[2])

exp = str(input()).split(" ")
day_exp = int(exp[0])
month_exp = int(exp[1])
year_exp = int(exp[2])

fine = 0

if year_act > year_exp:
    fine = 10000
elif year_act == year_exp:
    if month_act > month_exp:
        fine = (month_act - month_exp) * 500
    elif month_act == month_exp and day_act > day_exp:
        fine = (day_act - day_exp) * 15

print(fine)