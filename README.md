![CI](https://github.com/matteo4diani/poetry-packaging-demo/actions/workflows/ci.yml/badge.svg)

# poetry-packaging-demo

__CI-CD__ pipeline for Python projects consisting of:
1. A placeholder __Quality__ job that you can fill up with your favorite linters, formatters and testing frameworks.
2. A __Release__ job that releases to GitHub and publishes to PyPI using [python-semantic-release](https://python-semantic-release.readthedocs.io/en/latest/index.html) and [poetry](https://python-poetry.org).

Our pipeline automates [semantic versioning](https://semver.org) and distribution of Python projects by leveraging [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/#summary).

To use this demo in your project: 
1. Copy the `[tool.semantic_release]` section of our `pyproject.toml` into your `pyproject.toml` and adjust it to your project.
2. Copy the workflow file at `.github/workflows/ci.yml` into your `.github/workflows` folder and adjust it to your project.
3. In your repository's [Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository) create a token named `PYPI_TOKEN` and paste your [PyPI Token](https://pypi.org/help/#apitoken) into it.

Happy hacking 🐈‍⬛
