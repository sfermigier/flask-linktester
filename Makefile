.PHONY: test check tox lint clean tidy doc install upload

SRC=flask_linktester

all: test lint doc check

#
# testing
#
test:
	nosetests tests

test-with-coverage:
	nosetests --with-coverage --cover-erase --cover-package=$(SRC) tests

test-with-profile:
	nosetests --with-profile tests

tox:
	tox

lint:
	flake8 $(SRC) tests

travis:
	travis-solo

#
# Install
#
install:
	pip install --no-deps .

doc:
	sphinx-build -W -b html docs/ docs/_build/html

#
# Everything else
#
clean:
	find . -name "*.pyc" | xargs rm -f
	find . -name .DS_Store | xargs rm -f
	rm -rf *.egg-info *.egg .coverage
	rm -rf doc/_build build dist

tidy: clean
	rm -rf .tox
	rm -rf .travis-solo

upload:
	python setup.py sdist upload
