"""
This is the file in which we runs the program.
"""
from utility_package.utility_firstweek import Utility

nums = [4, 6, 2, 3, 1, -5]
# num = int(input("How many numbers you want in a list : "))
# list = [int(input()) for x in range (num)]

Utility.bubble_sort_a(nums)
print(nums)