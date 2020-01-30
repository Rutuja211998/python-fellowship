import unittest
from utility_package.utility_firstweek import Utility


class test_prime_fact(unittest.TestCase):
    def test_primefactors(self):
        n = 15
        expect = [3, 5]
        result = Utility.prime_fac(n)
        self.assertEqual(expect, result)


