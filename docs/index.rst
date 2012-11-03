Flask-LinkTester
****************

.. module:: flask_linktester

The **Flask-LinkTester** extension provides unit testing utilities for
`Flask`_.

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

TODO


Running tests
=============

with unittest
-------------

For the beginning I go on the theory that you put all your tests into one file
than you can use the :func:`unittest.main` function. This function will
discover all your test methods in your :class:`TestCase` classes. Remember, the
test methods and classes must starts with ``test`` (case-insensitive) that they
will discover.

An example test file cloud look like this::

    import unittest
    import flask.ext.testing

    # your test cases

    if __name__ == '__main__':
        unittest.main()

Now you can run your tests with ``python tests.py``.

with nose
---------

The `nose`_ collector and test runner works also fine with Flask-LinkTester.

Changes
=======

* **0.1 (2012/11/03)**

  * Extracted and refactored from the Abilian project.


API
===

.. module:: flask_linktester

.. autoclass:: LinkTester
   :members:

.. _Flask: http://flask.pocoo.org
.. _nose: http://nose.readthedocs.org/en/latest/
