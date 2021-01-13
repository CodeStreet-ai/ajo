# Ajo
Intelligent finance app based on Barefoot Investor.

## Development
---
### 1. clone the git repo:
```shell
git clone git@github.com:CodeStreet-ai/ajo.git
```
### 2. Change directory to ajo:
```shell
cd ajo
```
It is advisable to create python virtual environment for this project. Tool like [pyenv](https://github.com/pyenv/pyenv) and [poetry](https://python-poetry.org/docs/) are easy to use to create python env.

### 3. Create your branch:
Name your branch based on the feature you are working on. For example, Writing ReadMe branch would be called `feature/write_readme`:
```shell
git checkout -b <your branch name>
```

### 4. Install dependences:
if `poetry` is installed on your local machine, kindly run:
```shell
poetry install
```

**Or**
```shell
make install
```
###  5. Test
---
```shell
make tests
```
### 6. Run the app:
```shell
poetry run uvicorn ajo.main:app --reload
```
**Or**

```shell
uvicorn ajo.main:app --reload
```
### 7. Copy below links to your browser (Chrome):
To see index page:
```html
http://localhost:8000   
```
To see login page:
```html
http://localhost:8000/login
```
To see home page:
```html
http://localhost:8000/home
```

