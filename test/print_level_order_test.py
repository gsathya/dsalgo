import unittest

from lib import bst
from algo import print_level_order, sorted_array_to_bst

class TestPrintLevelOrder(unittest.TestCase):
    def setUp(self):
        self.bst = bst.BST()

    def test_add(self):
        vals = range(7)
        
        sorted_array_to_bst.convert(vals, 0, len(vals)-1, self.bst)
        print_level_order.print_tree(self.bst.root)
