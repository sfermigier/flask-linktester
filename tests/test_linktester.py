from __future__ import absolute_import

from flask_testing import TestCase

from flask_linktester import LinkTester

from .dummy_app import create_app


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

    def test_utf8_and_entities(self):
        """Ensure parser don't crash when parsing attributes with non-ascii
        characters + html entities.
        """
        self.crawler.crawl("/utf8_and_entities")


class VerboseLinkTester(BaseTestCase):

    def test_ok(self):
        self.crawler.verbosity = 3
        self.crawler.crawl("/ok")
