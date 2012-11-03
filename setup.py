"""
Flask-LinkTester
----------------

TODO.
"""

from setuptools import setup


tests_require = [
  'Flask',
  'Flask-Testing',
]

classifiers = [
  'Development Status :: 3 - Alpha',
  'Environment :: Web Environment',
  'Intended Audience :: Developers',
  'License :: OSI Approved :: BSD License',
  'Operating System :: OS Independent',
  'Programming Language :: Python',
  'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
  'Topic :: Software Development :: Libraries :: Python Modules'
]

setup(
  name='Flask-LinkTester',
  version='0.1',
  url='http://github.com/sfermigier/flask-linktester',
  license='BSD',
  author='Stefane Fermigier',
  author_email='sf@fermigier.com',
  description='Link tester for Flask applications',
  long_description=__doc__,
  packages=['flask_linktester'],
  test_suite="tests.suite",
  zip_safe=False,
  platforms='any',
  tests_require=tests_require,
  classifiers=classifiers,
)
