# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 23:03:51 2023

@author: LENOVO
"""

class Student:
    pass
class Marks:
    pass
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Marks))
print(isinstance(marks1, Student))
print(isinstance(student1, Marks))
print()
print("to check if the said classes are subclasses of the built in object class or not.\n")
print(issubclass(Student, object))
print(issubclass(Marks, object))
