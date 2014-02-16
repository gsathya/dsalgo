import unittest

from algo import binary_add

class TestEditDistance(unittest.TestCase):
    def test_edit_dist(self):
        num1 = "01"
        num2 = "111"
        self.assertEqual(int(binary_add.add(num1, num2), 2), int(num1, 2)+int(num2, 2))

        num1 = "0"
        num2 = "111"
        self.assertEqual(int(binary_add.add(num1, num2), 2), int(num1, 2)+int(num2, 2))

        num1 = "0"
        num2 = "111"
        self.assertEqual(int(binary_add.add(num1, num2), 2), int(num1, 2)+int(num2, 2))

        num1 = "111"
        num2 = "111"
        self.assertEqual(int(binary_add.add(num1, num2), 2), int(num1, 2)+int(num2, 2))

        num1 = "01"
        num2 = "0"
        self.assertEqual(int(binary_add.add(num1, num2), 2), int(num1, 2)+int(num2, 2))

        num1 = "0"
        num2 = "0"
        self.assertEqual(int(binary_add.add(num1, num2), 2), int(num1, 2)+int(num2, 2))

        num1 = "11111"
        num2 = "1"
        self.assertEqual(int(binary_add.add(num1, num2), 2), int(num1, 2)+int(num2, 2))
