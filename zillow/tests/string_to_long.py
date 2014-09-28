import unittest

import stringToLong

class TestStringToLong(unittest.TestCase):
    def setUp(self):
        self.convert = stringToLong.convert

    def test_conversion(self):
        self.assertEqual(self.convert("123"), 123)
        self.assertEqual(self.convert("-10"), -10)

    def test_exceptions(self):
        self.assertRaises(TypeError, self.convert, 123)
        self.assertRaises(TypeError, self.convert, 123.01)
        self.assertRaises(ValueError, self.convert, '')

    def test_zeroes(self):
        self.assertEqual(self.convert("0"), 0)
        self.assertEqual(self.convert("000000"), 0)
