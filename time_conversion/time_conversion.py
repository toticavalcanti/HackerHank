# -*- coding: utf-8 -*-
"""
@author: toti.cavalcanti
"""

#!/bin/python3

def solution(hour):
    hour = hour.split(':')
    if 'p' in hour[2].lower():
        if hour[0] == '12':
            hour = ':'.join(hour)
            return hour[:-2]
        else:
            hour[0] = str(int(hour[0]) + 12)
            hour = ':'.join(hour)
            return hour[:-2]
    elif hour[0] == '12':
        hour[0] = '00'
        hour = ':'.join(hour)
        return hour[:-2]
    else:
        hour = ':'.join(hour)
        return hour[:-2]

