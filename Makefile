.PHONY: test check tox lint clean tidy doc install upload


SRC=flask_linktester

all: test lint doc check

#
# testing
#
test:
	pytest tests

test-with-coverage:
	pytest --with-coverage --cover-erase --cover-package=$(SRC) tests

test-with-profile:
	pytest --with-profile tests

tox:
	tox

lint:
	flake8 $(SRC) tests *.py
	pylint --py3k $(SRC) tests *.py

travis:
	travis-solo

format:
	isort -rc *.py $(SRC) tests
	yapf --style google -r -i *.py $(SRC) tests
	isort -rc *.py $(SRC) tests

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
	rm -rf __pycache__

tidy: clean
	rm -rf .tox
	rm -rf .travis-solo

upload:
	python setup.py sdist upload
