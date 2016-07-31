# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 17:39:10 2016

@author: pcarl_000
"""

# Element Search

def elementSearch(mylist, val):
    '''Uses binary search to find a value within a string'''
    sorted_list = sorted(mylist)
    found = False
    start = 0
    end = len(sorted_list) - 1
    while start <= end and not found:
    
        mid = int((end + start)/2)
        print(mid)
        if val == sorted_list[mid]:
            found = True
        elif val < sorted_list[mid]:
            end = sorted_list[mid] - 1
            print(end)
        else:
            start = sorted_list[mid] + 1
            print(start)
    return found
#    return sorted_list, found, start, end

            
print(elementSearch([2,3,1,4,5,3,2], 5))

            
'''a = [1,3,4,5,6,6]
mid = int(len(a)/2)
a = a[:mid]
print(a)'''
