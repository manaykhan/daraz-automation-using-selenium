# Daraz Automation Tests

This repository contains a set of end-to-end automation tests for Daraz Pakistan ([https://www.daraz.pk/](https://www.daraz.pk/)), implemented using Selenium WebDriver and pytest following the Page Object Model (POM) design pattern.

## Table of Contents

* [Features](#features)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Running Tests](#running-tests)
* [Writing Additional Tests](#writing-additional-tests)

## Features

1. **Search Flow**: Navigate to Daraz, search for an item (e.g., "electronics").
2. **Price Filter**: Filter results by minimum and maximum price (500–5000).
3. **Result Count Validation**: Verify that the number of items found is greater than zero.
4. **Product Selection**: Click on the first product in the results.
5. **Free Shipping Check**: Assert if the selected product offers free shipping.

## Prerequisites

* Python 3.7 or higher
* Google Chrome browser

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/manaykhan/daraz-automation-using-selenium.git
   cd daraz-automation-using-selenium
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

Execute all tests with:

```bash
pytest -q
```

* `-q` (quiet) reduces pytest output noise.
* To see debug `print()` statements, use:

  ```bash
  pytest -q -s
  ```

## Writing Additional Tests

1. Create a new Page Object in `pages/` for any new page or component.
2. Add test functions to `tests/test_*.py` or create new test files.
3. Use fixtures in `conftest.py` for reusable setup (e.g., login flows).
