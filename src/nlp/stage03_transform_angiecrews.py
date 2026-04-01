"""
stage03_transform_angiecrews.py

Source: validated JSON object
Sink: Polars DataFrame
"""

import logging
from typing import Any

import polars as pl


def run_transform(
    json_data: list[dict[str, Any]],
    LOG: logging.Logger,
) -> pl.DataFrame:
    """Transform JSON into a structured DataFrame for the custom pipeline."""
    LOG.info("========================")
    LOG.info("STAGE 03: TRANSFORM (angiecrews) starting...")
    LOG.info("========================")

    records: list[dict[str, Any]] = []

    # Updated field mapping for /comments endpoint (Option A)
    for record in json_data:
        records.append(
            {
                "post_id": record["postId"],
                "comment_id": record["id"],
                "name": record["name"],
                "email": record["email"],
                "body": record["body"],
            }
        )

    df: pl.DataFrame = pl.DataFrame(records)

    # Add derived metrics (Options B and existing body metrics)
    df = df.with_columns(
        [
            pl.col("name").str.len_chars().alias("name_length"),
            pl.col("name").str.count_matches(r"\S+").alias("name_word_count"),
            pl.col("body").str.len_chars().alias("body_length"),
            pl.col("body").str.count_matches(r"\S+").alias("body_word_count"),
        ]
    )

    # Option C: filter to records with a body longer than 150 characters
    before_count = len(df)
    df = df.filter(pl.col("body_length") > 150)
    after_count = len(df)
    LOG.info(
        f"Filter applied: body_length > 150 — kept {after_count} of {before_count} records."
    )

    # Option D: log summary statistics for key numeric columns
    LOG.info(
        f"body_word_count stats: "
        f"min={df['body_word_count'].min()}, "
        f"max={df['body_word_count'].max()}, "
        f"mean={df['body_word_count'].mean():.1f}"
    )

    LOG.info("Transformation complete.")
    LOG.info(f"DataFrame preview:\n{df.head()}")
    LOG.info("Sink: Polars DataFrame created")

    return df
