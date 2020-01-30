"""
This is the test case class for testing Balanced Parentheses.
Author : Rutuja Tikhile
Date : 24/01/2020
"""
import unittest
from utility_package.utility_secondweek import BalancedParentheses


class test_balanced(unittest.TestCase):
    def test_balance(self):
        string = "(5+6)*(7+8)/(4+3)(5+6)*(7+8)/(4+3)"
        expect = True
        result = BalancedParentheses().balanced_parentheses(string)
        self.assertEqual(expect, result)

    def test_balance1(self):
        string = "(5+6)*(7+8)"
        expect = True
        result = BalancedParentheses().balanced_parentheses(string)
        self.assertEqual(expect, result)

    def test_balance2(self):
        string = "(7+8)/(4+3)"
        expect = True
        result = BalancedParentheses().balanced_parentheses(string)
        self.assertEqual(expect, result)

    def test_balance3(self):
        string = "{(a+b)}"
        expect = True
        result = BalancedParentheses().balanced_parentheses(string)
        self.assertEqual(expect, result)

