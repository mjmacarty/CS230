# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 10:18:08 2021

@author: mmacarty
"""


# Program to calculate income
WEEKS = 50

print("Welcome to Income calculator")
hourly_wage = float(input("Enter hourly wage: "))

print("Enter hours per week worked:")
hours_per_week = int(input())

weekly_income = hourly_wage * hours_per_week
annual_income = weekly_income * WEEKS
monthly_income = annual_income / 12

print("Weekly income: ", weekly_income)
print("Monthly income: ", monthly_income)
print("Annual income: ", annual_income)










