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
	openfisca test -c openfisca_senegal openfisca_senegal/tests/ -i depenses_ht_poste_3_2_1_1_1, depenses_ht_tva_taux_normal, tva_taux_normal, tva, impots_indirects, indirect_taxes
	pytest