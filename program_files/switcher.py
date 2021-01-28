# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 10:36:57 2021

@author: mmacarty
"""

print("enter a number`")
A = input()
B = input("Enter another number: ")

print("You entered A = " + B)
print("You entered B = " + A)

# temp = A
# A = B
# B = temp

A, B = B, A

print("But I Switched them!")
print("A is now " + A)
print("B is now " + B)






