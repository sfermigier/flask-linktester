# Workaround a PyCharm bug
import sys
sys.path = [".."] + sys.path

from flask.ext.linktester import LinkTester
from flask.ext.testing import TestCase

from dummy_app import create_app


class BaseTestCase(TestCase):

  def create_app(self):
    return create_app()

  def setUp(self):
    self.crawler = LinkTester(self.client)
    self.crawler.black_list.add("/blacklisted")
    self.crawler.black_list.add("/dark*")


class TestLinkTester(BaseTestCase):

  def test_ok(self):
    self.crawler.crawl("/ok")

  def test_ko(self):
    try:
      self.crawler.crawl("/ko")
      self.fail("Should have raised an AssertionError")
    except AssertionError:
      pass


class VerboseLinkTester(BaseTestCase):

  def test_ok(self):
    self.crawler.verbosity = 3
    self.crawler.crawl("/ok")
