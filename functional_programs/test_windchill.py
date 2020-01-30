import unittest
from utility_package.utility_firstweek import Utility


class test_windchill(unittest.TestCase):
    def test_wind_chill(self):
        t, v = 4, 5
        expect = -5.81
        result = Utility.wind_chill(t, v)
        self.assertEqual(expect, result)


