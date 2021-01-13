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

### 3. Install dependences:
if `poetry` is installed on your local machine, kindly run:
```shell
poetry install
```

**Or**
```shell
make install
```
### 4. Run the app:
```shell
poetry run uvicorn ajo.main:app --reload
```
**Or**

```shell
uvicorn ajo.main:app --reload
```
## Test
---
```shell
make tests
```
