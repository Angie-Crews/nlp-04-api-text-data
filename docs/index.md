# Web Mining and Applied NLP

This site provides documentation for this project.
Use the navigation to explore module-specific materials.

## How-To Guide

Many instructions are common to all our projects.

See
[⭐ **Workflow: Apply Example**](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to get these projects running on your machine.

## Project Documentation Pages (docs/)

- **Home** - this documentation landing page
- **Project Instructions** - instructions specific to this module
- **Glossary** - project terms and concepts

## Phase 4: Technical Modification (angiecrews)

Applied 5 technical modifications to the example pipeline:

- **Endpoint changed** from `/posts` to `/comments`
- **Validation strengthened** with required-key and blank-text checks for `/comments` fields (`postId`, `name`, `email`, `body`)
- **Derived columns added**: `name_word_count` and `body_word_count`
- **Row filter applied**: kept only comments with `body_length > 150` (312 of 500 records)
- **Summary stats logged**: `body_word_count` min/max/mean on every run

Output: `data/processed/angiecrews_comments_processed.csv` (312 rows × 9 columns)

## Phase 5: New API Problem — /users (angiecrews)

Applied the same EVTL pipeline to the `/users` endpoint to answer:
**"Who are the users behind the posts?"**

Key techniques demonstrated:

- **Nested JSON flattening**: extracted `address.city` and `company.name` from nested objects
- **Derived field**: `email_domain` split from the `email` field on `@`
- **Structure inspection logging**: all nested keys reported during Validate

Pipeline files:

| File | Purpose |
|---|---|
| `src/nlp/config_angiecrews_users.py` | API URL and output paths for `/users` |
| `src/nlp/stage02_validate_angiecrews_users.py` | Validates nested user records |
| `src/nlp/stage03_transform_angiecrews_users.py` | Flattens nested JSON, derives `email_domain` |
| `src/nlp/pipeline_api_json_angiecrews_users.py` | Phase 5 pipeline entry point |

Output: `data/processed/angiecrews_users_processed.csv` (10 rows × 9 columns:
`user_id`, `name`, `username`, `email`, `phone`, `website`, `city`, `company_name`, `email_domain`)
