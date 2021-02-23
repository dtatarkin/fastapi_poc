# fastapi_poc

## Overview
Proof of concept REST API backend app. Based on [FastAPI](https://fastapi.tiangolo.com/).

## Installation

Prerequisites:
 1. [pyenv](https://github.com/pyenv/pyenv#installation)
 1. [pipenv](https://github.com/pyenv/pyenv#installation)

### 1. Install dependencies
```bash
pipenv shell
pipenv install
```

### 2. Run server
```bash
uvicorn main:app --reload
```

Look at [API documentation](http://127.0.0.1:8000/redoc)

Try API here: [Swagger](http://127.0.0.1:8000/docs)
 
 
## Development

### Organize imports
    isort -m3 -tc -l120

### Lint
    mypy .
    prospector

### Test
    pytest

# Drawbacks
 - Hardcoded discounts, taxes, US states (no Admin Site)
 - Lack of documentation
