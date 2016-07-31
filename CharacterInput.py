# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 15:08:58 2016

@author: pcarl_000
"""

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
times = int(input("Please enter then number of times to print your future age: "))
age += 100
pstring = "Hi " + name + " you will be " + str(age) + " in 100 years.\n"
print(times * pstring)