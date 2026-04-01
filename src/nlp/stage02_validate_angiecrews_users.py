"""
stage02_validate_angiecrews_users.py

Source: raw JSON object from /users endpoint
Sink: validated JSON object
"""

import logging
from typing import Any


def run_validate(
    json_data: Any,
    LOG: logging.Logger,
) -> list[dict]:
    """Inspect and validate JSON structure for the users pipeline."""
    LOG.info("========================")
    LOG.info("STAGE 02: VALIDATE (angiecrews_users) starting...")
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
            LOG.info(f"  {key}: {type(value).__name__}")
        LOG.info("Nested address keys:")
        for key, value in first_record.get("address", {}).items():
            LOG.info(f"  address.{key}: {type(value).__name__}")
        LOG.info("Nested company keys:")
        for key, value in first_record.get("company", {}).items():
            LOG.info(f"  company.{key}: {type(value).__name__}")

    if not isinstance(json_data, list):
        raise ValueError("Expected JSON data to be a list of records.")

    if len(json_data) == 0:
        raise ValueError("Expected at least one record.")

    if not all(isinstance(record, dict) for record in json_data):
        raise ValueError("Expected each record to be a dictionary.")

    # Required top-level keys for /users endpoint
    required_keys = {"id", "name", "username", "email", "address", "company"}
    missing_key_indexes: list[int] = []
    blank_text_indexes: list[int] = []

    for idx, record in enumerate(json_data):
        missing_keys = required_keys - set(record.keys())
        if missing_keys:
            missing_key_indexes.append(idx)
            continue

        name = record.get("name")
        email = record.get("email")
        if (
            not isinstance(name, str)
            or not name.strip()
            or not isinstance(email, str)
            or not email.strip()
        ):
            blank_text_indexes.append(idx)

    if missing_key_indexes:
        LOG.warning(f"Records missing required keys at indexes: {missing_key_indexes}")

    if blank_text_indexes:
        LOG.warning(
            f"Records with blank name or email at indexes: {blank_text_indexes}"
        )

    invalid_indexes = set(missing_key_indexes) | set(blank_text_indexes)
    valid_records = [r for i, r in enumerate(json_data) if i not in invalid_indexes]

    LOG.info(
        f"Validation complete: {len(valid_records)} of {len(json_data)} records passed."
    )
    LOG.info("Sink: validated JSON object")

    return valid_records
