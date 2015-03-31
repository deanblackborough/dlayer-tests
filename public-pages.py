import unittest

# Import tests
from public.Home import Home
from public.WhatIsDlayer import WhatIsDlayer
from public.HistoryOfDlayer import HistoryOfDlayer
from public.DevelopmentPlan import DevelopmentPlan
from public.DevelopmentLog import DevelopmentLog
from public.Bugs import Bugs
from public.SvnReleasePolicy import SvnReleasePolicy

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(Home))
    test_suite.addTest(unittest.makeSuite(WhatIsDlayer))
    test_suite.addTest(unittest.makeSuite(HistoryOfDlayer))
    test_suite.addTest(unittest.makeSuite(DevelopmentPlan))
    test_suite.addTest(unittest.makeSuite(DevelopmentLog))
    test_suite.addTest(unittest.makeSuite(Bugs))
    test_suite.addTest(unittest.makeSuite(SvnReleasePolicy))
    return test_suite

if __name__ == "__main__":
    #So you can run tests from this module individually.
    unittest.main()   