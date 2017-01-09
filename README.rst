Flask-LinkTester
================

Check links for your Flask app during integration tests, when using
Flask-Testing.

Sample code:

::

    class TestLinkTester(TestCase):

        def create_app(self):
            ...

        def test_links_from_home(self):
          crawler = LinkTester(self.client, "/")
          crawler.crawl()

For full information please refer to the online docs:

http://packages.python.org/Flask-LinkTester
