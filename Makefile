.PHONY: install run format test

install:
	pip install -r requirements.txt
	python3 -m pip install --upgrade pip
	echo "-dependencies installed"

test:
	pytest

run:
	python ./main.py
	echo "-server is running"

format:
	black .
	echo "-code is formatted with black"
	ruff .
	echo "-code is formatted with ruff"
