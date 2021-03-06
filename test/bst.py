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

        self.assertEqual(self.bst.find_min(), min(vals))

    def test_height(self):
        vals = [3, 4, 4, 5, 8, 2]

        for val in vals:
            self.bst.add(val)

        self.assertEqual(self.bst.find_height(), 4)

    def test_delete(self):
        vals = [3, 4, 4, 5, 8, 2]

        for val in vals:
            self.bst.add(val)

        for val in vals:
            self.bst.delete(val)
            self.assertFalse(self.bst.has_value(val))

        for val in reversed(vals):
            self.bst.add(val)

        for val in vals:
            self.bst.delete(val)
            self.assertFalse(self.bst.has_value(val))

        for val in vals:
            self.bst.add(val)

        for val in reversed(vals):
            self.bst.delete(val)
            self.assertFalse(self.bst.has_value(val))
