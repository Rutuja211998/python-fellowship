"""
This is the file in which we runs the program.
"""
from utility_package.utility_firstweek import Utility

year = int(input("Enter year: "))

Utility.leap_year(year)
print(year)
