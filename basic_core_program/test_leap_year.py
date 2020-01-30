import unittest
from utility_package.utility_firstweek import Utility


class test_leap_year(unittest.TestCase):

    def test_leap(self):
        year = 2020
        expect = "Leap year"
        result = Utility.leap_year(year)
        self.assertEqual(expect, result)

    def test_not_leap(self):
        year = 2019
        expect = "Not a Leap year"
        result = Utility.leap_year(year)
        self.assertEqual(expect, result)

    def four_digit_number(self):
        year = 542067788
        expect = "Ensure it is a 4 digit number."
        result = Utility.leap_year(year)
        self.assertEqual(expect, result)


