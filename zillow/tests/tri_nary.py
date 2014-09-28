import unittest

import triNary

class TrinaryTreeTest(unittest.TestCase):
    def setUp(self):
        self.tree = triNary.Tree()

    def test_insert(self):
        input_values = [5, 4, 9, 5, 7, 2, 2]
        max_value = max(input_values)
        min_value = min(input_values)

        for value in input_values:
            # insert value
            self.tree.insert(value)

            # has it been inserted?
            self.assertTrue(self.tree.has_value, value)

            # is it still a valid tri-nary tree?
            self.assertTrue(self.tree.is_tri_nary, (max_value, min_value, None))

    def test_delete(self):
        input_values = [5, 4, 9, 5, 7, 2, 2]
        max_value = max(input_values)
        min_value = min(input_values)

        # insert values into tree first
        for value in input_values:
            self.tree.insert(value)

        for value in input_values:
            # delete value
            self.tree.delete(value)

            # is it still a valid tri-nary tree?
            self.assertTrue(self.tree.is_tri_nary, (10, 0, None))

    def test_empty_tree_delete(self):
        # delete from an empty tree
        self.assertRaises(Exception, self.tree.delete, 10)
