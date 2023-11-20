.PHONY: install run format lint

install:
    @pip install -r requirements.txt
    @python -m pip install --upgrade pip
    @echo "-dependencies installed"

test:
    @pip install pytest
	
run:
    @python main.py
    @echo "-server is running"

format:
    @black main.py
    @echo "-code is formatted with black"

    @ruff main.py.
    @echo "-code is formatted with ruff"

clean:
    @pip uninstall -y -r requirements.txt
    @rm -rf .pytest_cache
    @find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
    @echo "-cleaned up"
