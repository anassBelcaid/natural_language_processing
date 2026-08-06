# Project 01: The NLP Time Machine

This folder contains the complete starter kit for CS 351 Project 01.

## Files

- `nlp_time_machine.py` — the project implementation. This is the only Python
  file you are expected to modify. Replace the three `NotImplementedError`
  statements under the "Your implementation" comments.
- `test_nlp_time_machine.py` — the public autograder. Do not modify this file.
  Use it repeatedly while implementing and debugging your functions.
- `pyproject.toml` — the Python package requirements and pytest configuration.
  `uv` reads this file when creating the project environment.
- `uv.lock` — the exact dependency versions used to test the starter. Keep it
  beside `pyproject.toml` so that installations remain reproducible.
- `README.md` — this guide.

## Setup

Open a terminal in this directory and run:

```bash
uv sync
```

This creates an isolated `.venv` and installs the required packages. You do not
need to activate the environment when commands are prefixed with `uv run`.

## Run the autograder

Before implementing the functions:

```bash
uv run pytest -q
```

The starter should report seven expected failures and one passing
infrastructure test. As you complete the functions, rerun either the entire
suite or one focused group:

```bash
uv run pytest -q -k tokenize
uv run pytest -q -k lexicon
uv run pytest -q
```

A complete implementation should report:

```text
8 passed
```

## Optional Transformer demonstration

Transformer inference is not part of the deterministic autograder. To run the
optional demonstration, install its additional dependencies:

```bash
uv add transformers torch
```

This command modifies `pyproject.toml` and `uv.lock` in your personal copy,
which is acceptable.

## Submission checklist

Submit:

1. Your completed `nlp_time_machine.py`
2. The output of `uv run pytest -q`
3. A Markdown comparison table containing five model disagreements
4. A 150–250 word conclusion answering the question on the homework page

Do not submit `.venv`, `__pycache__`, or `.pytest_cache` directories.
