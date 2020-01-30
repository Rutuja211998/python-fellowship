"""
This is the test case class for testing prime anagrams.
Author : Rutuja Tikhile
Date : 27/01/2020
"""
import unittest
from data_structure_programs.prime_anagram import primes


class prime(unittest.TestCase):
    def test_prime(self):
        a = primes(1000)
        expect = primes()
        result = primes()

        self.assertEqual(expect, result)

