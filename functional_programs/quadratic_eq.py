"""
This is the file in which we runs the program.
"""
from utility_package.utility_firstweek import Utility

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

z = Utility.quadratic(a, b, c)
print(z)