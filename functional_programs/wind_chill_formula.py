from utility_package.utility_firstweek import Utility

t = int(input("Enter t: "))
v = int(input("Enter v: "))

a = Utility.wind_chill(t, v)
print("Wind chill: ", a)