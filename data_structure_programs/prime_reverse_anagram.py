from data_structure_programs.anagram_of_prime import primes
from data_structure_programs.anagram_of_prime import anagram
"""
This is the file in which we runs the program.
Author:Rutuja Tikhile.
Date: 25/01/2020.
"""
a = primes(1000)
# anagrams = a[:1000]
anagrams = a[::-1]
print("The Anagram elements from 0 to 1000 are listed :", anagram(anagrams))