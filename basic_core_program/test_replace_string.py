import unittest
from utility_package.utility_firstweek import Utility


class test_replace_string(unittest.TestCase):

    def test_replace(self):
        string = "rutuja"
        expect = "Hello Rutuja, How Are You?"
        result = Utility.string_replace(string)
        self.assertEqual(expect, result)

    def test_replace_min_3(self):
        string = "sd"
        expect = "Hello Sd, How Are You?"
        result = Utility.string_replace(string)
        self.assertEqual(expect, result)

    def test_not_numeric(self):
        string = "123456"
        expect = "Hello 123456, How Are You?"
        result = Utility.string_replace(string)
        self.assertEqual(expect, result)
