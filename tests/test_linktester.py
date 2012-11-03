from flask.ext.linktester import LinkTester
from flask.ext.testing import TestCase

from dummy_app import create_app


class TestLinkTester(TestCase):

    def create_app(self):
        return create_app()

    def test_ok(self):
      crawler = LinkTester(self.client, "/")
      crawler.crawl()

    def test_ko(self):
      crawler = LinkTester(self.client, "/ko")
      try:
        crawler.crawl()
        self.fail("Should have raised an AssertionError")
      except AssertionError:
        pass
