# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 23:02:41 2023

@author: LENOVO
"""

def palindrome(string):
    if string[::-1] == string:
        return True
    else :
        return  False



string = str(input('enter a string :- \n'))
string1 = string.lower() and string.replace(' ', '')
a = palindrome(string1)
if a == True :
    print(f'{string} is a palindrome.')
else :
    print(f'{string} is not a palindrome.')