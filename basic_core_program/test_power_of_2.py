import unittest
from utility_package.utility_firstweek import Utility


class test_power(unittest.TestCase):
    def test_power_2(self):
        expo = 3
        expect = [2, 4, 8]
        result = Utility.power_of2(expo)
        self.assertEqual(expect, result)

    def test_power_of_2(self):
        expo = 4
        expect = [2, 4, 8, 16]
        result = Utility.power_of2(expo)
        self.assertEqual(expect, result)