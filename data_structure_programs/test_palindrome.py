"""
This is the test case class for testing Palindrome.
Author : Rutuja Tikhile
Date : 24/01/2020
"""
import unittest
from utility_package.utility_secondweek import PalindromeChecker


class test_palindrome(unittest.TestCase):
    def test_palindrome(self):
        string = "nitin"
        expect = True
        result = PalindromeChecker().palindromeChecker(string)
        self.assertEqual(expect, result)

    def test_palindrome1(self):
        string = "madam"
        expect = True
        result = PalindromeChecker().palindromeChecker(string)
        self.assertEqual(expect, result)

    def test_palindrome2(self):
        string = "tomot"
        expect = True
        result = PalindromeChecker().palindromeChecker(string)
        self.assertEqual(expect, result)

    def test_palindrome3(self):
        string = "aabbaa"
        expect = True
        result = PalindromeChecker().palindromeChecker(string)
        self.assertEqual(expect, result)