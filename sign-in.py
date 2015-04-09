import unittest

# Import tests
from signIn.Home import Home
from signIn.User1 import User1
from signIn.User2 import User2
from signIn.User3 import User3

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(User1))
    test_suite.addTest(unittest.makeSuite(User2))
    test_suite.addTest(unittest.makeSuite(User3))
    return test_suite

if __name__ == "__main__":
    #So you can run tests from this module individually.
    unittest.main()   