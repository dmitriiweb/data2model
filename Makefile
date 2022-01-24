.PHONY: test
test:
	pytest --cov=data_to_model -vv tests/
	flake8 data_to_model tests/
	mypy data_to_model
	black data_to_model tests/
	isort data_to_model tests/

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
