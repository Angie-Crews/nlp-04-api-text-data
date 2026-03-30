# nlp-01-getting-started

[![Python 3.14+](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](#)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Professional Python project for Web Mining and Applied NLP.

Web Mining and Applied NLP focus on retrieving, processing, and analyzing text from the web and other digital sources.
This course builds those capabilities through working projects.

In the age of generative AI, durable skills are grounded in real work:
setting up a professional environment,
reading and running code,
understanding the logic,
and pushing work to a shared repository.
Each project follows a similar structure based on professional Python projects.
These projects are **hands-on textbooks** for learning Web Mining and Applied NLP.

## This Project

This project focuses on retrieving and processing structured text data
**from web APIs in JSON format**.

The goal is to acquire JSON data from an external source,
inspect and validate its structure,
transform it into a usable format,
and load it into a reproducible output.

You've likely heard of ETL or ELT.
We recommend EVTL.

In EVTL, each stage has a source, a process, and a sink.

- **Extract** acquires data
- **Validate** inspects and checks it
- **Transform** reshapes it
- **Load** sends it to the chosen destination

This project illustrates how to **work with real API data and understand its structure before analysis**.

## Key Files

You'll work with these files as you update authorship and experiment:

- **src/nlp/pipeline_api_json.py** - MAIN PIPELINE SCRIPT (no changes needed)
- **src/nlp/config_case.py** - Python configuration (<mark>**copy and edit**</mark> for your custom project)
- **src/nlp/stage01_extract.py** - EXTRACT (no changes needed)
- **src/nlp/stage02_validate_case.py** - VALIDATE (<mark>**copy and edit**</mark>)
- **src/nlp/stage03_transform_case.py** - TRANSFORM (<mark>**copy and edit**</mark>)
- **src/nlp/stage04_load.py** - LOAD (no changes needed)
- **pyproject.toml** - <mark>**update**</mark> authorship, links, and dependencies
- **zensical.toml** - <mark>**update**</mark> authorship and links

## First: Follow These Instructions

Follow the [step-by-step workflow guide](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/) to complete:

1. Phase 1. **Start & Run**
2. Phase 2. **Change Authorship**
3. Phase 3. **Read & Understand**

## Success

After running the script successfully, you will see:


```shell
========================
Pipeline executed successfully!
========================
```

And new files will appear:

- project.log - confirming successful run
- data/raw/case_raw.json - dump of the fetched JSON
- data/processed/case_processed.csv - final loaded result

## Command Reference

The commands below are used in the workflow guide above.
They are provided here for convenience.

Follow the guide for the **full instructions**.

<details>
<summary>Show command reference</summary>

### In a machine terminal (open in your `Repos` folder)

After you get a copy of this repo in your own GitHub account,
open a machine terminal in your `Repos` folder:

```shell
# Replace username with YOUR GitHub username.
git clone https://github.com/Angie-Crews/nlp-04-api-text-data
cd nlp-04-api-text-data
code .
```

### In a VS Code terminal

```shell
uv self update
uv python pin 3.14
uv sync --extra dev --extra docs --upgrade

uvx pre-commit install
git add -A
uvx pre-commit run --all-files

# repeat if changes were made
git add -A
uvx pre-commit run --all-files

# Later, we install spacy data model and
# en_core_web_sm = english, core, web, small
# It's big: spacy+data ~200+ MB w/ model installed
#           ~350–450 MB for .venv is normal for NLP
# uv run python -m spacy download en_core_web_sm

# First, run the module
# IMPORTANT: Close each figure after viewing so execution continues
uv run python -m nlp.pipeline_api_json

uv run ruff format .
uv run ruff check . --fix
uv run zensical build

git add -A
git commit -m "update"
git push -u origin main
```

</details>

## Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.

## Example Artifact (Output)



```text
START PIPELINE
ROOT_PATH = .
DATA_PATH = data
RAW_PATH = data\raw
PROCESSED_PATH = data\processed
========================
STAGE 01: EXTRACT starting...
========================
SOURCE PATH = https://jsonplaceholder.typicode.com/posts
SINK PATH = data\raw\case_raw.json
========================
STAGE 02: VALIDATE starting...
========================
JSON STRUCTURE INSPECTION:
Top-level type: list
Keys in first record: ['userId', 'id', 'title', 'body']
Field types:
userId: int
id: int
title: str
body: str
Validation passed.
Sink: validated JSON object
========================
STAGE 03: TRANSFORM starting...
========================
Transformation complete.
DataFrame preview:
shape: (5, 6)
...preview of dataframe...
Sink: Polars DataFrame created
========================
STAGE 04: LOAD starting...
========================
SINK PATH = data\processed\case_processed.csv
========================
Pipeline executed successfully!
========================
```


## Enhancements

In production systems, validation is often automated using tools
such as Great Expectations or Soda.

In this module, validation is implemented manually to develop a
clear understanding of structure, assumptions, and data quality.

## Phase 1: Start & Run (Completed)

The project has been completed using Workflow 2.1 steps:

1. [Start in GitHub to Copy a Template Repository](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/01-start-and-run/01-start-in-github/)
2. [Configure Repository Settings](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/01-start-and-run/02-configure-repo-settings/)
3. [Clone the Repository To Your Machine](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/01-start-and-run/03-clone-repo-to-local/)
4. [Open the Project in VS Code (and Install Recommended VS Code Extensions)](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/01-start-and-run/04-open-vscode-extensions/)
5. [Set up Project Python Environment (managed by uv)](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/01-start-and-run/05-set-up-environment/)
6. [Run the Project Code](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/01-start-and-run/06-run-project/)
7. [Git add-commit-push](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/01-start-and-run/07-git-add-commit-push/)

Phase 1 outcome achieved:

- Working project copy in GitHub
- Local clone on machine
- Python environment set up with uv
- Project run completed successfully
- Commit pushed to GitHub

## Phase 2: Change Authorship

Phase 2. Make the project yours while preserving credit for the original.

Goal:

In this phase, you update the project to reflect your authorship. The repository now belongs to you while crediting the original source.

Steps:

1. [Git pull before changes](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/02-change-authorship/01-git-pull-before-changes/)
2. [Update authorship and repository references](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/02-change-authorship/02-update-authorship/)
3. [Run the project code](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/02-change-authorship/03-run-project/)
4. [Git add-commit-push](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/02-change-authorship/04-git-add-commit-push/)

## Phase 3: Read & Understand the Project

Phase 3. Read and understand the tools and techniques used in the project.

Professional Practice:

Before modifying a project, first read and understand how it works.

Professional developers often explore a project in a consistent order: documentation, code, data, and outputs.

Focus on the overall flow of the project. It's not necessary to understand every line of code at this point.

Professional Project Organization:

Real-world projects contain many files, so most professional projects follow a predictable organization.

Folder Naming Conventions:

When referring to a folder in documentation, a / is often added to the name. For example, data/.

The slash is not part of the folder name - it just indicates a folder.

Goal:

By the end of this phase you should understand:

- the purpose of the project
- the main tools or techniques used
- how data flows through the program

Suggested Reading Order:

1. README.md (root project folder)

   Overview of the project, description of the problem and approach, and instructions for running the project.

2. Documentation (docs/)

   Explanations of the project and descriptions of techniques used.

3. Notebooks and Source Code (notebooks/ and src/)

   Jupyter notebooks usually run from top to bottom.

   Python modules are typically stored in src/. Execution often begins at an entry point near the end of the file:


   ```python
   def main():
       # This is where execution logic begins

   if __name__ == "__main__":
       main()
   ```

   When reading a Python file:

   - locate the main() function
   - observe which functions are called
   - follow how information flows through the program
   - note what is passed to each function as arguments (inside the parentheses)

4. Data (data/)

   Explore the input datasets and observe how data is used in the program.

5. Outputs (artifacts/ or output/)

   Review generated results, charts, or reports.

6. Log File (project.log)

   Shows what the program did during execution, helps with debugging, and confirms the program was executed successfully.
