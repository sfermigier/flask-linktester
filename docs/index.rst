
Flask-LinkTester
================

The **Flask-LinkTester** extension helps test there are no invalid links on a
`Flask`_ application. This is specially useful for websites, and can also
be used as smoke tests for applications.

.. _Flask: http://flask.pocoo.org/


Installing Flask-LinkTester
---------------------------

Install with **pip** and **easy_install**::

    pip install Flask-LinkTester

or download the latest version from version control::

    git clone https://github.com/sfermigier/flask-linktester.git
    cd flask-linktester
    python setup.py develop

If you are using **virtualenv**, it is assumed that you are installing
**Flask-LinkTester** in the same virtualenv as your Flask application(s).


Using
-----

Here's how you would write your tests::

    class CheckLinkTestCase(TestCase):

        def create_app(self):
            ...

        def test_links_from_home(self):
          crawler = LinkTester(self.client, "/")
          crawler.crawl()

If, for some reason, you know some of your links will fail but you want to run
the tests anyway, you can blacklist some links by adding::

          crawler.black_list |= ['/bad', '/another/bad/*']



Changes
-------

* **0.2.3 (2014/04/22)**

  * Don't track urls starting with '//'.

* **0.2 (2013/10/21)**

  * Small cleanups + first release on PyPi.

* **0.1 (2012/11/03)**

  * Extracted and refactored from the `Abilian`_ project.

.. _Abilian: http://www.abilian.com/


API
---

.. module:: flask_linktester

.. autoclass:: LinkTester
   :members:


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
