import unittest

import test.bst
import test.sorted_array_to_bst
import test.edit_distance
import test.binary_search
import test.print_level_order_test
import test.binary_add_test
import test.linked_list_test

suite = unittest.TestLoader()
suite = suite.loadTestsFromModule(test.bst)
suite.addTest(unittest.TestLoader().loadTestsFromModule(test.sorted_array_to_bst))
suite.addTest(unittest.TestLoader().loadTestsFromModule(test.edit_distance))
suite.addTest(unittest.TestLoader().loadTestsFromModule(test.binary_search))
#suite.addTest(unittest.TestLoader().loadTestsFromModule(test.print_level_order_test))
suite.addTest(unittest.TestLoader().loadTestsFromModule(test.binary_add_test))
suite.addTest(unittest.TestLoader().loadTestsFromModule(test.linked_list_test))

if __name__ == "__main__":
  unittest.TextTestRunner().run(suite)
