"""
This is the test case class for testing Ordered list.
Author : Rutuja Tikhile
Date : 24/01/2020
"""

import unittest
from utility_package.utility_weeksecond import OrderedList


class test_order(unittest.TestCase):

    def test_orderedlist(self):
        a = 44
        expect = "Not found"
        result = OrderedList.orderedList(a)
        self.assertEqual(expect, result)


