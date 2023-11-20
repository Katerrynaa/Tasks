.PHONY: install run format

install:
    @pip install -r requirements.txt
    @python -m pip install --upgrade pip
    @echo "-dependencies installed"

test:
    pytest 
	
run:
    @python main.py
    @echo "-server is running"

format:
    @black main.py
    @echo "-code is formatted with black"

    @ruff main.py
    @echo "-code is formatted with ruff"

