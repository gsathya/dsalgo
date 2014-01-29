import unittest

from algo import edit_dist

class TestBST(unittest.TestCase):
    def test_edit_dist(self):
        self.assertEqual(edit_dist.edit_distance("cat", "bat"), 1)
        self.assertEqual(edit_dist.edit_distance("cat", "catt"), 1)
        self.assertEqual(edit_dist.edit_distance("bat", "catt"), 2)            
