# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 15:55:34 2016

@author: pcarl_000
"""

num = int(input("Please enter a number: "))

if num % 4 == 0:
    numtype = 'evenly divisible by four'
elif num % 2 == 0:
    numtype = 'even'
else:
    numtype = 'odd'
    
print('Your number is ' + numtype + '.')
    