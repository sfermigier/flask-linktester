import unittest
from tests.test_linktester import TestLinkTester


def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(TestLinkTester))
  return suite
