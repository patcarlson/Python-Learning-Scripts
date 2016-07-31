# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 14:19:17 2016

@author: pcarl_000
"""

def largestnum (var1,var2,var3):
    if var1 > var2:
        if var1 > var3:
            return var1
    elif var2 > var3:
        return var2
    else:
        return var3
        
theanswer = largestnum(34000000,23549898989898,2342315)
print(theanswer)