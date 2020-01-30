import unittest
from utility_package.utility_firstweek import Utility


class test_quadratic(unittest.TestCase):
    def test_quadratic_eq(self):
        a, b, c = 1, 2, 3
        expect = ((-1-1.4142135623730951j), (-1+1.4142135623730951j))
        result = Utility.quadratic(a, b, c)
        self.assertEqual(expect, result)


if __name__ == '__main__':
    unittest.main()
