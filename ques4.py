# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 23:03:14 2023

@author: LENOVO
"""

def pangram(string):
    for i in range(65,91) :
        if chr(i) and chr(i).lower() in string :
            continue
        else :
            return False

string = str(input('enter a string :- \n'))

a = pangram(string)

if a == False :
    print('It is not a pangram.')
else :
    print('It is a pangram.')
