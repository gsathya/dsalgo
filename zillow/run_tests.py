import unittest

import tests.tri_nary
import tests.string_to_long

if __name__ == "__main__":
    suite = unittest.TestLoader()
    suite = suite.loadTestsFromModule(tests.tri_nary)
    suite.addTest(unittest.TestLoader().loadTestsFromModule(tests.string_to_long))

    unittest.TextTestRunner().run(suite)
