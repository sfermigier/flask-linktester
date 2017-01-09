"""
Flask-LinkTester
----------------

TODO.
"""
from __future__ import absolute_import

from setuptools import setup

VERSION = "0.3.0"

REQUIREMENTS = [
    'Flask',
    'requests',
]

TESTS_REQUIREMENTS = REQUIREMENTS + [
    'pytest',
    'Flask-Testing',
    'flake8',
    'pylint',
    'sphinx',
]

CLASSIFIERS = [
    'Development Status :: 4 - Beta', 'Environment :: Web Environment',
    'Intended Audience :: Developers', 'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent', 'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Python Modules'
]


def get_long_description():
    return open("README.rst").read()


if __name__ == '__main__':
    setup(
        name='Flask-LinkTester',
        version=VERSION,
        url='http://github.com/sfermigier/flask-linktester',
        license='BSD',
        author='Stefane Fermigier',
        author_email='sf@fermigier.com',
        description='Link tester for Flask applications',
        long_description=get_long_description(),
        packages=['flask_linktester'],
        zip_safe=False,
        platforms='any',
        install_requires=REQUIREMENTS,
        extras_require={'testing': TESTS_REQUIREMENTS,},
        classifiers=CLASSIFIERS,)
