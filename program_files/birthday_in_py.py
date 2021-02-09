import sympy
def find_birthday(birthdate, digits=1e5):
    pi = str(sympy.N(sympy.pi, digits))
    if pi.find(birthdate) >0:
        return pi.find(birthdate)
    else:
        return f"{birthdate} not found in first {digits:,.0f} digits of pi"