lint:
	tox -e lint

test:
	tox

build:
	rm -rf dist
	tox -e build

test-deploy: dist
	tox -e deploy

deploy: dist
	tox -e prod-deploy
