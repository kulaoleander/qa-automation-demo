# QA Automation Demo with Selenium and Pytest

![CI](https://github.com/kulaoleander/qa-automation-demo/actions/workflows/ci.yml/badge.svg)

A UI test automation project built with Python, Selenium, and Pytest.

The project demonstrates browser automation, reusable Page Object Model components, test reporting, and automated execution through GitHub Actions.

## Test Scenarios

### Bing Search

- opens the Bing search page;
- enters a search query;
- submits the search;
- verifies that the results page is displayed.

### HerokuApp Login

- tests a successful login flow;
- tests an unsuccessful login flow;
- verifies the resulting success or error message.

### SauceDemo Shopping Flow

- opens the product page;
- selects a product;
- adds the product to the cart;
- verifies that the cart state is updated.

## Technical Features

- Python-based UI automation;
- Selenium WebDriver;
- Pytest test organization and execution;
- Page Object Model structure;
- explicit waits for more stable browser interaction;
- logging for test execution and debugging;
- HTML test reports with `pytest-html`;
- GitHub Actions CI triggered by repository updates.

## Test Workflow

```text
Start test suite
↓
Launch browser
↓
Open target website
↓
Perform user actions
↓
Verify page state and expected results
↓
Generate HTML report
↓
Run automatically in GitHub Actions
```

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/kulaoleander/qa-automation-demo.git
cd qa-automation-demo
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the tests

```bash
pytest -q
```

### 5. Generate an HTML report

```bash
pytest -q --html=reports/report.html --self-contained-html
```

The generated report is saved to:

```text
reports/report.html
```

## Continuous Integration

The GitHub Actions workflow automatically installs the project dependencies and runs the test suite when configured repository events occur.

The CI badge at the top of this README shows the latest workflow status.

## Skills Demonstrated

- browser-based test automation;
- reusable test architecture;
- positive and negative test scenarios;
- automated verification with assertions;
- test reporting;
- CI-based test execution;
- Python project organization.
