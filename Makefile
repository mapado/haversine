.DEFAULT_GOAL := help

## clean: Clean directory for build
clean:
	rm -rf dist/*

.PHONY: build
## build: Build package
build:
	pipenv run python setup.py sdist bdist_wheel

## deploy: Deploy haversine to pypi
deploy: clean build
	pipenv install twine
	pipenv run twine upload dist/*
	pipenv uninstall twine
	git checkout -- Pipfile.lock


.PHONY: help
## help: Prints this help text.
help:
	@echo ''
	@echo '  Usage:'
	@echo '    make <target>'
	@echo ''
	@echo '  Targets:'
	@sed -n 's/^## \?/    /p' $(MAKEFILE_LIST)
