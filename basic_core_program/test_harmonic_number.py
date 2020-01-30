import unittest
from utility_package.utility_firstweek import Utility


class test_harmonic_number(unittest.TestCase):
    def test_harmonic(self):
        n = 5
        expect = 2.283333333333333
        result = Utility.nth_harmonic(n)
        self.assertEqual(expect, result)

    def test_harmonic(self):
        n = 2
        expect = 1.5
        result = Utility.nth_harmonic(n)
        self.assertEqual(expect, result)