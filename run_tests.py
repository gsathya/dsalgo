import unittest

import test.bst
import test.sorted_array_to_bst
import test.edit_distance

suite = unittest.TestLoader()
suite = suite.loadTestsFromModule(test.bst)
suite.addTest(unittest.TestLoader().loadTestsFromModule(test.sorted_array_to_bst))
suite.addTest(unittest.TestLoader().loadTestsFromModule(test.edit_distance))

if __name__ == "__main__":
  unittest.TextTestRunner().run(suite)
