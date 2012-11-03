"""
Flask-LinkTester
----------------

TODO.
"""

import sys
from setuptools import setup

tests_require = [
    'Flask',
    'Flask-Testing',
]

if sys.version_info < (2, 6):
    tests_require.append('simplejson')

setup(
    name='Flask-LinkTester',
    version='0.1',
    url='TODO',
    license='BSD',
    author='Stefane Fermigier',
    author_email='sf@fermigier.com',
    description='Link tester for Flask',
    long_description=__doc__,
    packages=['flask_linktester'],
    test_suite="tests.suite",
    zip_safe=False,
    platforms='any',
    tests_require=tests_require,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
