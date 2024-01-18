.PHONY: install run format test db

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
	black . --exclude /alembic/*
	echo "-code is formatted with black"
	ruff . --fix --exclude /alembic/*
	echo "-code is formatted with ruff"

db:
	alembic upgrade head

revision:
	@read -p "Enter the message: " msg; \
	msg=`echo $$msg | tr '[ ]' '[_]'`; \
	alembic revision --autogenerate -m $$msg
