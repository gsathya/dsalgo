import unittest

from algo import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_edit_dist(self):
        arr = [0, 1, 2, 3, 4, 4, 4, 5, 5, 6, 10]
        self.assertEqual(binary_search.begining_search(arr, 4), 4)
        self.assertEqual(binary_search.binary_search(arr, 4), 5)
        self.assertEqual(binary_search.end_search(arr, 4), 6)
