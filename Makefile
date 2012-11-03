.PHONY: test tox pep8 clean

SRC=flask_linktester

all: test pep8

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

#
# Install
#
install:
	pip install -I --no-deps .

#
# Everything else
#
pep8:
	pep8 -r --ignore E111,E225,E501,E127 *.py $(SRC) tests

clean:
	find . -name "*.pyc" | xargs rm -f
	find . -name .DS_Store | xargs rm -f
	rm -rf *.egg-info *.egg .coverage
	rm -rf doc/_build build dist

tidy: clean
	rm -rf .tox

