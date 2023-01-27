# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 23:02:17 2023

@author: LENOVO
"""

def perfect(num):
    a = []

    for i in range(1,num):

        if num % i == 0:
            a.append(i)
    b = sum(a)

    if num == b:
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")


num = int(input("Enter any number to check if it is perfect or not :- \t"))
c = perfect(num)