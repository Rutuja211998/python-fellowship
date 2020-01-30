"""
This is the file in which we runs the program.
Author: Rutuja Tikhile.
Date: 20/01/2020.
"""
from utility_package.utility_secondweek import PalindromeChecker

p = PalindromeChecker()
string = input("Enter string : ").replace(" ", "")

result = p.palindromeChecker(string)
if result:
    print("String is palindrome.")
else:
    print("String is not palindrome.")