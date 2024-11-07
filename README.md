# Fetch Receipt Challenge 2025
#### Kenneth Zhou

Server runs at `http://localhost:8000`

### Installation instructions: 

#### With docker:
1. In root directory, run `docker compose build` and `docker compose up`

#### Without docker: 
1. Install `python 3.11`
2. In root directory, run `pip install -r requirements.txt`
3. Run `uvicorn src:app --proxy-headers --host 0.0.0.0 --port 8000`

### Notes:
- Server runs at http://localhost:8000
- By default, the server is set up to print a warning if receipt is suspicious (receipt total is different from sum of items or price values are negative). This can be set to return a 404 error if `THROW_ON_VALIDATION_ERROR` is set to `True` in `src/router.py`