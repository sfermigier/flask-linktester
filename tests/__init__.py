from __future__ import absolute_import

import unittest

from .test_linktester import TestLinkTester


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestLinkTester))
    return suite
