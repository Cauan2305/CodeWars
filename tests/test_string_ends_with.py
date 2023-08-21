from kyu_august.string_ends_with.main  import solution
import unittest

class TestStringEndsWith(unittest.TestCase):

    def test_positive_cases(self):
        self.assertTrue(solution('abc', 'bc'))
        self.assertTrue(solution('hello', 'lo'))
        self.assertTrue(solution('world', 'd'))
        self.assertTrue(solution('CodeWars', 'Wars'))

    def test_negative_cases(self):
        self.assertFalse(solution('abc', 'd'))
        self.assertFalse(solution('hello', 'world'))
        self.assertFalse(solution('CodeWars', 'code'))

    def test_edge_cases(self):
        # When the ending string is empty, it should always return True
        self.assertTrue(solution('abc', ''))
        # When both strings are empty
        self.assertTrue(solution('', ''))
        # When the main string is shorter than the ending string
        self.assertFalse(solution('abc', 'abcd'))
