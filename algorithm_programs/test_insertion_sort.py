import unittest
from utility_package.utility_firstweek import Utility


class test_sorting(unittest.TestCase):
    def test_insertion_sort(self):
        list = [4, 2, 1, 5, 3]
        expect = [1, 2, 3, 4, 5]
        result = Utility.insertion_sort_a(list)
        self.assertEqual(expect, result)
