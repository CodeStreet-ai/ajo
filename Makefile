all: install tests clean

PIP := pip

TEST := pytest

install:
		@echo "Install dependent packages ..."
		${PIP} install -r requirements/requirements.txt
		${PIP} install -r requirements/requirements-dev.txt

test:
		@echo "testing ..."
		${TEST} tests

clean:
		find . 	-name '__pycache__' -exec rm -rf {} +
		find . -name '*pyc' -exec rm -rf {} +
		find . -name '.DS_Store' -exec rm -rf {} +
