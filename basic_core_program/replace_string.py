"""
This is the file in which we runs the program.
"""
from utility_package.utility_firstweek import Utility

string = input("Username: ")
string = string.strip()  # .strip method removes any leading (spaces at the beginning)
# and trailing (spaces at the end) in a string.
a = Utility.string_replace(string)
print(a)

