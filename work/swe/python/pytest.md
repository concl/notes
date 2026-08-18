
Reference: https://docs.pytest.org/en/stable/reference/reference.html

## Running tests

Running tests with standard test discovery from the current directory (or in testpaths, if configured from the pyproject.toml) (searches recursively for files of the form `test_*.py` and `*_test.py`):

```bash
pytest
```

Running tests from specific directories:

```bash
pytest path/to/directory path/to/dir2 ...
```

Running specific file:

```bash
pytest -q test_add.py
```

Running specific class from specific file:

```bash
pytest -q test_add.py -k TestVectorAdd
```

Configuring pytest from `pyproject.toml`:

We can set the testpaths config option as follows:
```toml
[pytest]
testpaths = ["testing", "doc"]
```

## Writing tests

Every test file that is discovered by pytest (`test_*.py`, ...) should define functions and classes that implement a test (usually consisting of running some input against some code, and asserting some condition).

Functions (defined at the root of the program) that are prefixed with `test_` are automatically discovered as tests.

Multiple tests can be grouped into a class, (which should be prefixed with `Test`, like `TestFoo`), for which each method that defines a test will be ran (prefixed with `test_`).

Example test:
```python
# test_add.py

import pytest

def test_add():
	assert 1 + 1 == 2
	
def bad_func():
	return "Bad"	

# failing test
def test_add_bad():
	assert bad_func() == "Good"
```
