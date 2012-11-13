.PHONY: test check tox pep8 clean tidy doc install

SRC=flask_linktester

all: test pep8 doc check

#
# testing
#
test:
	python -m unittest discover -s tests

test-with-coverage:
	nosetests --with-coverage --cover-erase --cover-package=$(SRC) tests

test-with-profile:
	nosetests --with-profile tests

tox:
	tox

pep8:
	pep8 -r --ignore E111,E121,E225,E501,E127 *.py $(SRC) tests

check:
	travis-lint .travis.yml

#
# Install
#
install:
	pip install --no-deps .

doc:
	python setup.py build_sphinx

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

