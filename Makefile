.PHONY: install run format test migration migrate-up

install:
	pip install -r requirements.txt
	python -m pip install --upgrade pip
	echo "-dependencies installed"

test:
	pytest -s -v --cov=./ --cov-report term-missing

run:
	python ./main.py
	echo "-server is running"

format:
	black . --exclude '/alembic/'
	echo "-code is formatted with black"
	ruff . --exclude '/alembic/'
	echo "-code is formatted with ruff"

migration:
	alembic revision --autogenerate -m "Create table"


migrate-up:
	alembic upgrade head


