version := $(shell python -c 'from data2model import __version__; print(__version__)')


.PHONY: test
test:
	pytest --cov=data_to_model -vv tests/

.PHONY: docs-serve
docs-serve:
	mkdocs serve

.PHONY: docs-publish
docs-publish:
	mkdocs mkdocs gh-deploy --force

.PHONY: publish
publish:
	poetry build
	poetry publish
