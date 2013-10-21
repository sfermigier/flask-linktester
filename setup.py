"""
Flask-LinkTester
----------------

TODO.
"""

from setuptools import setup

requirements = [
  'Flask',
  'requests',
]
tests_requirements = [
  'Flask-Testing',
  'pep8',
  'travis-solo',
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


def get_long_description():
  """
  Hack to provide a ``.rst`` description to PyPI even when the ``README`` is
  actually written using Markdown.
  """

  import os

  if os.path.exists("README.rst"):
    return open("README.rst").read()
  elif os.path.exists("README.md"):
    rst = os.popen("pandoc -r markdown -w rst -o - README.md").read()
    if rst:
      return rst
    else:
      return open("README.md").read()
  elif os.path.exists("README.txt"):
    return open("README.txt").read()
  else:
    return None


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
  install_requires=requirements,
  tests_require=tests_requirements,
  classifiers=classifiers,
)
