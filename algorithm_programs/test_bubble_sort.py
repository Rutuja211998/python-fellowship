import unittest
from utility_package.utility_firstweek import Utility


class test_bubble_sort(unittest.TestCase):
    def test_sort(self):
        list = [2, 1, 5, 3]
        expect = [1, 2, 3, 5]
        result = Utility.insertion_sort_a(list)
        self.assertEqual(expect, result)
        self.assertEqual(expect, result)



