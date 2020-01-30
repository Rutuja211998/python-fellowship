from data_structure_programs.anagram_of_prime import primes
from utility_package.utility_weeksecond import PrimeTwoDArray
from data_structure_programs.anagram_of_prime import anagram
"""
This is the file in which we runs the program.
Author:Rutuja Tikhile.
Date: 25/01/2020.
"""

obj = PrimeTwoDArray
obj.primes(1000)

print("The Prime Numbers are: ", primes(1000))
print()
a = primes(1000)

anagrams = a[0:25]
print("The Anagram elements from 0 to 100 are listed :", anagram(anagrams))
anagrams = a[25:50]
print("The Anagram elements from 100 to 200 are listed :", anagram(anagrams))
anagrams = a[50:75]
print("The Anagram elements from 200 to 400 are listed :", anagram(anagrams))
anagrams = a[75:100]
print("The Anagram elements from 400 to 500 are listed :", anagram(anagrams))
anagrams = a[100:125]
print("The Anagram elements from 500 to 600 are listed :", anagram(anagrams))
anagrams = a[125:150]
print("The Anagram elements from 600 to 900 are listed :", anagram(anagrams))
anagrams = a[150:175]
print("The Anagram elements from 900 to 1000 are listed :", anagram(anagrams))

# anagrams = a[:1000]
# print("The Anagram elements from 0 to 1000 are listed :", anagram(anagrams))