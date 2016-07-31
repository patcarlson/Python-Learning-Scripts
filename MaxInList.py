# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 11:23:41 2016

@author: pcarl_000
"""
s = 'ABCDCDC'
ss= 'CDC'
ln = len(ss)
counter = 0
for i in range(0,7):
    if s[i:i+ln] == ss:
        counter +=1
print(str(counter))

