___very new idea / very not working yet / come back later___

# packagify

## :snake: Python scripts :arrow_right: Package :package:

`npm init` but for Python. Takes a Python script (or a collection thereof) and generates a nice neat package with a `setup.py`

| Before                | After                      |
|-----------------------|----------------------------|
| `thingy.py`           | `thingy/__init__.py`       |
| `imported_file.py`    | `thingy/imported_file.py`  |
|                       | `setup.py`                 |

## Initial Ideas

- Dependencies
  - Imports are parsed to find local imports, e.g. if `import thingy` in code and `thingy.py` exists in directory
  - If imports aren't found locally, add to setup's `install_requires`
    - Could also check PyPI and output warning if package doesn't exist
- Setup fields
  - `name`: Defaults to input entry filename, minus `.py`
  - `version`: Defaults to 0.1.0 (not sure about this)
  - `description`: No default, prompt user
  - `long_description`: Defaults to README content if exists
  - `long_description_content_type`: 'text/markdown' if `README.md`, etc.
  - `url`: Defaults to git remote if exists, otherwise prompt
  - `author`: Defaults to git config name, otherwise prompt
  - `author_email`: Defaults to git config email, otherwise prompt
  - `python_requires`: Prompt user for minimum Python 3 version, default to 3.3
  - `classifiers`: Listed [here](https://pypi.org/pypi?%3Aaction=list_classifiers)
    - '`Programming Language :: Python :: {version}`' for every version allowed by `python_requires`
    - Prompt for '`Development Status`' and '`License`'
