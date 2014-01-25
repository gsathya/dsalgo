import unittest

import test.bst

suite = unittest.TestLoader()
suite = suite.loadTestsFromModule(test.bst)

if __name__ == "__main__":
  unittest.TextTestRunner().run(suite)
