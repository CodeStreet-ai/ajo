all: install tests clean app-start

RUN := poetry 

install: # install the dependencies
		@echo "Install dependent packages ..."
		${RUN} install 

test: # run test coverage
		@echo "testing ..."
		${RUN} run pytest --cov=. --cov-report html --hypothesis-show-statistics

quality: # run test, formating the code, check for typing, check if the code is safe
		@echo "check for linting, Typing, code formating, safety"
		${RUN} run tox -e py

app-start: # start the application
		${RUN} run uvicorn ajo.main:app --reload

clean:  # remove unwanted files and folders
		find . 	-name '__pycache__' -exec rm -rf {} +
		find . -name '*pyc' -exec rm -rf {} +
		find . -name '.DS_Store' -exec rm -rf {} +
