"""
This is the file in which we runs the program.
"""
from utility_package.utility_firstweek import Utility

stake = int(input("Enter stack: "))
goal = int(input("Enter goal: "))
trails = int(input("Enter trails: "))

Utility.gambler(stake, goal, trails)