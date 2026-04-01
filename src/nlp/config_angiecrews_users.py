"""
config_angiecrews_users.py

Configuration values for the Phase 5 EVTL pipeline targeting the /users endpoint.
"""

from pathlib import Path

# API CONFIGURATION
API_URL: str = "https://jsonplaceholder.typicode.com/users"

HTTP_REQUEST_HEADERS: dict[str, str] = {
    "User-Agent": "nlp-module-4-angiecrews/1.0",
    "Accept": "application/json",
}

# PATH CONFIGURATION
ROOT_PATH: Path = Path.cwd()
DATA_PATH: Path = ROOT_PATH / "data"
RAW_PATH: Path = DATA_PATH / "raw"
PROCESSED_PATH: Path = DATA_PATH / "processed"

RAW_JSON_PATH: Path = RAW_PATH / "angiecrews_users_raw.json"
PROCESSED_CSV_PATH: Path = PROCESSED_PATH / "angiecrews_users_processed.csv"
