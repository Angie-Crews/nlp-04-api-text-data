"""
stage03_transform_angiecrews_users.py

Source: validated JSON object from /users endpoint
Sink: Polars DataFrame

Demonstrates handling nested JSON (address, company objects)
and deriving a new field (email_domain).
"""

import logging
from typing import Any

import polars as pl


def run_transform(
    json_data: list[dict[str, Any]],
    LOG: logging.Logger,
) -> pl.DataFrame:
    """Transform /users JSON into a structured DataFrame."""
    LOG.info("========================")
    LOG.info("STAGE 03: TRANSFORM (angiecrews_users) starting...")
    LOG.info("========================")

    records: list[dict[str, Any]] = []

    for record in json_data:
        # Flatten nested address and company objects
        address: dict = record.get("address", {})
        company: dict = record.get("company", {})

        records.append(
            {
                "user_id": record["id"],
                "name": record["name"],
                "username": record["username"],
                "email": record["email"],
                "phone": record.get("phone", ""),
                "website": record.get("website", ""),
                "city": address.get("city", ""),
                "company_name": company.get("name", ""),
            }
        )

    df: pl.DataFrame = pl.DataFrame(records)

    # Derive email_domain by splitting on '@' and taking the second part
    df = df.with_columns(
        pl.col("email").str.split("@").list.get(1).alias("email_domain")
    )

    # Log summary stats for name field
    LOG.info(
        f"name_length stats: "
        f"min={df['name'].str.len_chars().min()}, "
        f"max={df['name'].str.len_chars().max()}, "
        f"mean={df['name'].str.len_chars().cast(pl.Float64).mean():.1f}"
    )

    # Log unique email domains
    domains = df["email_domain"].unique().sort().to_list()
    LOG.info(f"Unique email domains ({len(domains)}): {domains}")

    LOG.info("Transformation complete.")
    LOG.info(f"DataFrame preview:\n{df}")
    LOG.info("Sink: Polars DataFrame created")

    return df
