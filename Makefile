.DEFAULT_GOAL := help

## clean: Clean directory for build
clean:
	rm -rf dist/*

.PHONY: build
## build: Build package
build:
	pipenv install build --dev --skip-lock
	pipenv run python -m build

## deploy: Deploy haversine to pypi
deploy: clean build
	pipenv install twine
	pipenv run twine upload dist/* --verbose
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
