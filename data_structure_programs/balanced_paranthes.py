"""
This is the file in which we runs the program.
Author: Rutuja Tikhile.
Date: 21/01/2020.
"""
from utility_package.utility_secondweek import BalancedParentheses

obj = BalancedParentheses()
a = obj.balanced_parentheses
string = input("Enter expression : ")
# (5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)
print(a(string))