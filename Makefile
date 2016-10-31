all: test

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

test: check-syntax-errors flake8
	@# Launch tests from openfisca_senegal/tests directory (and not .) because TaxBenefitSystem must be initialized
	@# before parsing source files containing formulas.
	nosetests openfisca_senegal/tests --exe --with-doctest
