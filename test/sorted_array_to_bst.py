import unittest

from lib import bst
from algo import sorted_array_to_bst

class TestSortedArrayToBST(unittest.TestCase):
    def setUp(self):
        self.bst = bst.BST()

    def test_add(self):
        vals = range(7)

        sorted_array_to_bst.convert(vals, 0, len(vals)-1, self.bst)
