setup:
	python setup.py pytest

bdist_wheel:
	python setup.py bdist_wheel

install:
	pip install ./dist/hello-0.0.1-py3-none-any.whl
