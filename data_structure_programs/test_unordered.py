"""
This is the test case class for testing unordered list.
Author : Rutuja Tikhile
Date : 24/01/2020
"""
import unittest

from utility_package.utility_weeksecond import UnorderedList

#
# class test_unorder(unittest.TestCase):
#     def test_unordered(self):
#         a = "and"
#         expect = "found"
#         result = UnorderedList().unorderedList(a)
#         self.assertEqual(expect, result)

from utility_package.utility_secondweek import LinkedList


class test_insert(unittest.TestCase):
    def test_insertfun(self):
        llist = LinkedList()
        llist.insert(0)
        expext = (0)
        result = llist.display()
        self.assertEqual(expext, result)

