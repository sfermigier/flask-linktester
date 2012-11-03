Flask-LinkTester
****************

The **Flask-LinkTester** extension helps test there are no invalid links on a
`Flask`_ application.

Installing Flask-LinkTester
===========================

Install with **pip** and **easy_install**::

    pip install Flask-LinkTester

or download the latest version from version control::

    git clone https://github.com/sfermigier/flask-linktester.git
    cd flask-linktester
    python setup.py develop

If you are using **virtualenv**, it is assumed that you are installing
**Flask-LinkTester** in the same virtualenv as your Flask application(s).

Writing tests
=============

Here's how you would write your tests::

    class TestLinkTester(TestCase):

        def create_app(self):
            ...

        def test_links_from_home(self):
          crawler = LinkTester(self.client, "/")
          crawler.crawl()

If, for some reason, you know some of your links will fail but you want to run
the tests anyway, you can blacklist some links by adding::

          crawler.black_list |= ['/bad', '/another/bad/*']


Running tests
=============

with unittest
-------------

You can run the tests with the following command::

    python -m unittest discover -s tests

with nose
---------

The `nose`_ collector and test runner works also fine with Flask-LinkTester.

Changes
=======

* **0.1 (2012/11/03)**

  * Extracted and refactored from the `Abilian`_ project.


API
===

.. module:: flask_linktester

.. autoclass:: LinkTester
   :members:

.. _Flask: http://flask.pocoo.org/
.. _nose: http://nose.readthedocs.org/en/latest/
.. _Abilian: http://www.abilian.com/
