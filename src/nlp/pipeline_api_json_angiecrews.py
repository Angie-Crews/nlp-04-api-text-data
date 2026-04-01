"""
pipeline_api_json_angiecrews.py

Custom EVTL pipeline entry point that keeps the original case pipeline unchanged.

Run from the project root with:

    uv run python -m nlp.pipeline_api_json_angiecrews
"""

import logging

from datafun_toolkit.logger import get_logger, log_header, log_path

from nlp.config_angiecrews import (
    API_URL,
    DATA_PATH,
    HTTP_REQUEST_HEADERS,
    PROCESSED_CSV_PATH,
    PROCESSED_PATH,
    RAW_JSON_PATH,
    RAW_PATH,
    ROOT_PATH,
)
from nlp.stage01_extract import run_extract
from nlp.stage02_validate_angiecrews import run_validate
from nlp.stage03_transform_angiecrews import run_transform
from nlp.stage04_load import run_load

LOG: logging.Logger = get_logger("CI", level="DEBUG")


def main() -> None:
    log_header(LOG, "MODULE 4: EVTL PIPELINE (ANGIECREWS)")
    LOG.info("START PIPELINE")

    RAW_PATH.mkdir(parents=True, exist_ok=True)
    PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

    log_path(LOG, "ROOT_PATH", ROOT_PATH)
    log_path(LOG, "DATA_PATH", DATA_PATH)
    log_path(LOG, "RAW_PATH", RAW_PATH)
    log_path(LOG, "PROCESSED_PATH", PROCESSED_PATH)

    json_data = run_extract(
        source_api_url=API_URL,
        http_request_headers=HTTP_REQUEST_HEADERS,
        raw_json_path=RAW_JSON_PATH,
        LOG=LOG,
    )

    validated_data = run_validate(
        json_data=json_data,
        LOG=LOG,
    )

    df = run_transform(
        json_data=validated_data,
        LOG=LOG,
    )

    run_load(
        df=df,
        processed_csv_path=PROCESSED_CSV_PATH,
        LOG=LOG,
    )

    LOG.info("========================")
    LOG.info("Custom pipeline executed successfully!")
    LOG.info("========================")


if __name__ == "__main__":
    main()
