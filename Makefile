all: test

install:
	pip install --upgrade pip
	pip install -e .[dev]

check-syntax-errors:
	python -m compileall -q .

clean:
	rm -rf build dist
	find . -name '*.mo' -exec rm \{\} \;
	find . -name '*.pyc' -exec rm \{\} \;

flake8:
	@# Do not analyse .gitignored files.
	@# `make` needs `$$` to output `$`. Ref: http://stackoverflow.com/questions/2382764.
	flake8 `git ls-files | grep "\.py$$"`

pypi-upload:
	rm -rf dist/*
	python setup.py sdist bdist_wheel
	twine upload dist/*

test: check-syntax-errors
	flake8
	openfisca-run-test -c openfisca_senegal openfisca_senegal/tests/
