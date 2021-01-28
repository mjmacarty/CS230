# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 10:54:59 2021

@author: mmacarty
"""

TAX_RATE = .20
STANDARD_DEDUCTION = 12200
DEPENDENT_DEDUCTION = 2000

income = float(input("Enter your income: "))
dependents = int(input("Enter number of dependents: "))

taxable_income = income - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION * dependents
income_tax = taxable_income * TAX_RATE

#print("Your taxable income is: $", taxable_income)
print("Your taxable income is: $%.2f" % taxable_income)
print("Your taxable income is: ${:,.0f}".format(taxable_income,))
print(f"Your taxable income is: ${taxable_income:,.0f}")
print(f"Tax due: ${income_tax:,.0f}")


print(time.time())








