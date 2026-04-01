"""
stage02_validate_angiecrews.py

Source: raw JSON object
Sink: validated JSON object
"""

import logging
from typing import Any


def run_validate(
    json_data: Any,
    LOG: logging.Logger,
) -> list[dict]:
    """Inspect and validate JSON structure for the custom pipeline."""
    LOG.info("========================")
    LOG.info("STAGE 02: VALIDATE (angiecrews) starting...")
    LOG.info("========================")

    LOG.info("JSON STRUCTURE INSPECTION:")
    LOG.info(f"Top-level type: {type(json_data).__name__}")

    if (
        isinstance(json_data, list)
        and len(json_data) > 0
        and isinstance(json_data[0], dict)
    ):
        first_record = json_data[0]
        LOG.info(f"Keys in first record: {list(first_record.keys())}")
        LOG.info("Field types:")
        for key, value in first_record.items():
            LOG.info(f"{key}: {type(value).__name__}")

    if not isinstance(json_data, list):
        raise ValueError("Expected JSON data to be a list of records.")

    if len(json_data) == 0:
        raise ValueError("Expected at least one record.")

    if not all(isinstance(record, dict) for record in json_data):
        raise ValueError("Expected each record to be a dictionary.")

    # Updated required keys for /comments endpoint (postId, name, email instead of userId, title)
    required_keys = {"postId", "id", "name", "email", "body"}
    missing_key_indexes: list[int] = []
    blank_text_indexes: list[int] = []

    for idx, record in enumerate(json_data):
        missing_keys = required_keys - set(record.keys())
        if missing_keys:
            missing_key_indexes.append(idx)
            continue

        name = record.get("name")
        body = record.get("body")
        if (
            not isinstance(name, str)
            or not name.strip()
            or not isinstance(body, str)
            or not body.strip()
        ):
            blank_text_indexes.append(idx)

    if missing_key_indexes:
        sample = missing_key_indexes[:5]
        raise ValueError(
            f"Records missing required keys at indexes {sample}. Total failures: {len(missing_key_indexes)}"
        )

    if blank_text_indexes:
        sample = blank_text_indexes[:5]
        raise ValueError(
            f"Records with blank/non-string title/body at indexes {sample}. Total failures: {len(blank_text_indexes)}"
        )

    LOG.info(f"Validation passed for {len(json_data)} records.")
    LOG.info("Sink: validated JSON object")

    return json_data
