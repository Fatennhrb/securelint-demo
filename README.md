# SecureLint demo

A small project that shows [SecureLint](https://github.com/Fatennhrb/SecureLint)
checking pull requests as a GitHub Action.

- `main` holds one old problem in `inventory.py`. It is listed in
  `.securelint-baseline.json`, so it is known and does not fail the check.
- The pull request "Add an export command" adds two new problems. SecureLint
  shows them as notes on the changed lines:
  - a shell command built from typed input: high severity, so it **fails**
    the check (the policy in `pyproject.toml` blocks high and critical);
  - a hard-coded password: medium severity, so it is only a **warning**.

The workflow is in `.github/workflows/securelint.yml`.

The code in this repository is written to contain security problems on
purpose. Do not use it.
