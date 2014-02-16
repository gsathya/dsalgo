import unittest

from algo import binary_add

class TestEditDistance(unittest.TestCase):
    def test_edit_dist(self):
        self.assertEqual(int(binary_add.add("01", "111"), 2), int("01", 2)+int("111", 2))
