# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 23:03:24 2023

@author: LENOVO
"""

def hyphen(string):
    string1 = string.split("-")
    list1 = []

    for i in range(len(string1)) :
        b = string1[i]
        list1.append(b)
    list1.sort()
    c = str("-".join(list1))
    return c


string = str(input('Enter a string :- \n'))
a = hyphen(string)
print(a)
