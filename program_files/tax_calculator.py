"""
The tax calculator
"""

TAX_RATE = .20
STANDARD_DEDUCTION = 12200
DEPENDENT_DEDUCTION = 2000

print("Please enter your income: ")
income = float(input())
dependents = int(input("Please enter number of dependents: "))

taxable_income = income - STANDARD_DEDUCTION - dependents * DEPENDENT_DEDUCTION
tax_due = taxable_income * TAX_RATE

# print("Your taxable income is:", taxable_income)
# print("Your taxable income is: " + "$"+str(taxable_income))
# print("Your taxable income is $%.2f" % taxable_income)
# print("Your taxable income is ${:,.2f}".format(taxable_income))
print(f"Your taxable income is ${taxable_income:,.0f}")
print(f"Your tax due is ${tax_due:,.2f}")






