.PHONY: run publish-release run-e2e-tests

run:
	python3 setup.py sdist bdist_wheel
	pip3 install --force-reinstall .
	
run-e2e-tests:
	nose2 -s e2e-tests


publish-release:
	rm dist/ -r -f
	python3 setup.py sdist bdist_wheel
	python3 -m  twine upload -u "${PYPI_USERNAME}" -p "${PYPI_PASSWORD}" --repository-url https://upload.pypi.org/legacy/ dist/*
	@echo 'Do -> git tag -m "0.X.Y" -a 0.X.Y && git push --tags'
