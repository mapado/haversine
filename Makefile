.PHONY: build

clean:
	rm -rf dist/*

build:
	pipenv run python setup.py sdist bdist_wheel

deploy: clean build
	pipenv install twine
	pipenv run twine upload dist/*
	pipenv uninstall twine
