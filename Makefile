.PHONY: install run format

install:
    @pip install -r requirements.txt
    @echo "-dependencies installed"
	
run:
    @python main.py
    @echo "-server is running"

format:
    @black main.py.
    @echo "-code is formatted with black"

    @ruff main.py.
    @echo "-code is formatted with ruff"