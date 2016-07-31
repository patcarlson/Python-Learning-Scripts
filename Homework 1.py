# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Homework 1.1a and 1.1b
sentence = 'Discover, Learning, with, Edureka'
print("The number of lower case a's in '{}' is {} and the number of lower case o's is {}.".format(sentence, sentence.count('a'), sentence.count('o')))
print("The number of uppercase L's in {} is {} and the number of uppercase N's is {}.".format(sentence, sentence.count('L'), sentence.count('N')))


#Homework 2
#a
iadd = "www.edureka.in"
if iadd.find('w',0,iadd.index('.edureka.')) == -1 and iadd.find('w',iadd.index('.edureka.'),len(iadd)) == -1:
    print("No w's before or after '.edureka.'")
else: print(iadd.strip('w'))

#b
iadd = "www.edureka.in"
newstr = iadd.strip("[a-z]")
print(newstr)

