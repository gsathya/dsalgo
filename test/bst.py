import unittest

from lib import bst

class TestBST(unittest.TestCase):
    def setUp(self):
        self.bst = bst.BST()
    
    def test_add(self):
        vals = [3, 4, 4, 5, 8, 2]

        for val in vals:
            self.bst.add(val)

        for val in vals:
            self.assertTrue(self.bst.has_value(val))

    def test_find_min(self):
        vals = [3, 4, 4, 5, 8, 2]

        for val in vals:
            self.bst.add(val)
        
        self.bst.print_tree()
        self.assertEqual(self.bst.find_min(), 2)
