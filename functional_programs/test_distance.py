import unittest
from utility_package.utility_firstweek import Utility


class test_distance(unittest.TestCase):
    def test_dist(self):
        x, y = 1, 5
        expect = 5.0990195135927845
        result = Utility.distance(x, y)
        self.assertEqual(expect, result)


