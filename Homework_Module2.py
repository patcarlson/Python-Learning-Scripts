# -*- coding: utf-8 -*-
"""
Created on Thu May  5 12:42:18 2016

@author: pcarl_000
"""

#Changed raw_input() to input() because there is no raw_input() in 3.5
#Added parenthesis around the print statements.
"""total = input(r"What is the total amount for your online shopping?")
country = input(r'Shipping within the US or Canada?')
if country == "US": 
    if total <= "50": 
        print("Shipping Costs $6.00") 
    elif total <= "100": 
            print ("Shipping Costs $9.00") 
    elif total <= "150": 
            print ("Shipping Costs $12.00") 
    else: 
        print ("FREE") 
if country == "Canada": 
    if total <= "50": 
        print ("Shipping Costs $8.00") 
    elif total <= "100": 
        print ("Shipping Costs $12.00") 
    elif total <= "150": 
        print ("Shipping Costs $15.00") 
    else: 
        print ("FREE") """
        
#2. Write a program that uses raw_input to prompt a user for their name and then welcomes them.  
"""pname = input(r"Hi, what is your name?")
print("Hello{}!".format(pname))"""

#3. Write a program which prompts the user for a Fahrenheit temperature,
# convert the temperature to Celsius and print out the converted temperature

"""ftemp = input(r"Please enter the temperature in Fahrenheit.")
ctemp = 5/9*(ftemp-32)
print("{} degrees Fahrenheit is equal to {} degrees Celcius.".format(str(ftemp),str(ctemp)))"""

#4. Write a program to prompt the user for hours and rate per hour to compute gross pay.
"""hours = input(r"Please enter the number of hours worked.")
rate = input(r"Please enter the pay rate per hour.")
grosspay = int(hours)*int(rate)
print("Gross pay is equal to {}.".format(str(grosspay)))"""

#5. Write a for loop that prints all elements of a list and their position in the list.
'''l = ["blue", "red", "green", "yellow", "orange"]
i = 0
for i in l:
    print(l.index(i), i)'''
    
#6. Write a program which should create a dictionary of key:values.
'''mydictionary = {1:'one',2:'two',3:'three',4:'four'}
print(mydictionary)'''

#7. Write a program to reverse/inverse key:value like below. 
'''mydictionary = {1:'one',2:'two',3:'three',4:'four'}
inv_map = {k:v for v,k in mydictionary.items()}
print(inv_map)'''

#8. Using given list L = ['a', 'b', 'c', 'd'] create a dictionary of key:values.
l1 = [1,2,3,4]
l2 = ['a', 'b', 'c', 'd']
l3 = [l1,l2]
mydict = {}
for lists in l3:
    mydict[list[0]] = list[:]
print(mydict)