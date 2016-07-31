# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 11:49:21 2016

@author: pcarl_000
"""


#y= lambda x : print(x)
#z = list(map(y,range(1,x)))
#x = 5
#list(map(lambda x : print(x), range(1, x + 1)))

#9 number of students with Eng paper
#1 2 3 4 5 6 7 8 9 student id of english paper
#9 number of students with french paper
#10 1 2 3 11 21 55 6 8 student id with french paper

#numEng = input("Please enter the number of students that receive the English paper.")
#studentEng = set(input("Please enter the student ids of the students who receive the English paper separated by a space."))
#numFr = input("Please enter the number of students that receive the French paper.")
#studentFr = set(input("Please enter the student ids of the students who receive the French paper separated by a space."))
#newset = studentEng.union(studentFr)
#print(newset)
n = 2
l = "1 -1 -2 -1"
a = set(sorted(l.split()))
print(a)
#a = sorted(set(map(int,l)))
#if n >= 2:
#    print(a[-2])
#else:
#    print(None)