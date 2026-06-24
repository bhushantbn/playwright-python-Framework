# 🎭 Playwright Python Automation Framework

[![Python Version](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/playwright-v1.44+-green.svg)](https://playwright.dev/python/)
[![Pytest](https://img.shields.io/badge/pytest-v8.0+-red.svg)](https://docs.pytest.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

A modern, highly-scalable, hybrid test automation framework built using **Python**, **Playwright (Sync API)**, and **Pytest**. This framework is designed to test both **Web E2E UI** flows and **REST APIs**, adhering to software engineering best practices like the **Page Object Model (POM)** design pattern.

---

## 🚀 Key Features

*   🏗️ **Page Object Model (POM):** Clean separation of test cases and page-specific elements/actions, located in the [pages/](file:///d:/Python%20Projects/PlaywrightWebAutomation/pages) directory.
*   🌐 **E2E Web UI Testing:** Comprehensive test coverage of user flows, including authentication, cart actions, sorting verification, and hover effects on Swag Labs ([SauceDemo](https://www.saucedemo.com/)) and Amazon.
*   ⚡ **REST API Automation:** Integration tests covering `GET`, `POST`, and `PUT` methods against mock REST endpoints ([JSONPlaceholder](https://jsonplaceholder.typicode.com/)).
*   📊 **Aesthetic HTML Reporting:** Automatic, self-contained HTML test report generation via `pytest-html`, complete with custom stylesheet configuration ([assets/style.css](file:///d:/Python%20Projects/PlaywrightWebAutomation/assets/style.css)).
*   🔧 **Post-Execution Hooks:** Auto-opens generated test reports in your default web browser immediately after test completion via [conftest.py](file:///d:/Python%20Projects/PlaywrightWebAutomation/conftest.py).
*   ⚙️ **Robust Configuration:** Global properties for browser viewports, headless mode, slow-mo, timeouts, and automated screenshots/videos on failures managed under [config.py](file:///d:/Python%20Projects/PlaywrightWebAutomation/config.py).
*   🎯 **Custom Selector Engines:** Custom configured to prioritize `data-test` automation attributes.

---

## 📂 Project Architecture

```text
PlaywrightWebAutomation/
├── config/                 # Static configuration settings
│   └── settings.py         # Base environment configuration
├── pages/                  # Page Object classes (POM)
│   ├── login_page.py       # Actions & Locators for Login page
│   ├── Dashboard_page.py   # Actions & Locators for Inventory/Dashboard
│   └── cart_page.py        # Actions & Locators for Shopping Cart page
├── tests/                  # Automated Test Suites
│   ├── reports/            # Execution outputs & screenshots
│   ├── test_login.py       # UI Login scenarios
│   ├── test_dashboard.py   # UI Dashboard & Inventory scenarios
│   ├── test_cart.py        # UI Shopping Cart scenarios
│   ├── test_get_users.py   # API GET tests
│   ├── test_post_users.py  # API POST tests
│   └── test_update_user.py # API PUT tests
├── assets/                 # Style & custom layouts
│   └── style.css           # Custom styles for HTML reports
├── config.py               # Execution configurations (Slow-mo, Headless, Timeout, etc.)
├── conftest.py             # Global pytest fixtures and Hooks
├── e2etest.py              # Standalone E2E workflow script
├── pytest.ini              # Pytest execution properties and options
├── requirements.txt        # Python dependency requirements
└── readme.md               # Framework documentation
```

---

## 🛠️ Setup & Installation

Follow these steps to configure your local environment and run the test suites:

### 1. Prerequisites
Ensure you have **Python 3.8+** installed. You can download it from [python.org](https://www.python.org/downloads/).

### 2. Clone the Repository
```bash
git clone https://github.com/bhushantbn/playwright-python-Framework.git
cd playwright-python-Framework
```

### 3. Create and Activate a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
Install Pytest, Playwright, and reporting dependencies:
```bash
pip install pytest pytest-playwright pytest-html
```
*(Optionally: if you have a `requirements.txt` file, run: `pip install -r requirements.txt`)*

### 5. Install Playwright Browsers
Install required browser binaries (Chromium, Firefox, WebKit):
```bash
playwright install
```

---

## 🏃 Running Tests

The test runner utilizes **Pytest**. You can run tests under different configurations using standard CLI commands:

### Run All Test Suites
Runs both UI and API tests synchronously:
```bash
pytest
```

### Run Specific Test Suites
*   **UI Tests Only:**
    ```bash
    pytest tests/test_login.py
    pytest tests/test_dashboard.py
    pytest tests/test_cart.py
    ```
*   **API Tests Only:**
    ```bash
    pytest tests/test_get_users.py
    pytest tests/test_post_users.py
    ```

### Run Tests in Headed Mode (Visual execution)
By default, tests run in headless mode. Use the `--headed` flag to observe the browser execution:
```bash
pytest --headed
```

### Run Tests on Specific Browsers
```bash
# Chromium (Default)
pytest --browser chromium

# Firefox
pytest --browser firefox

# WebKit (Safari engine)
pytest --browser webkit
```

### Generate Custom HTML Reports
Generate a complete, self-contained HTML report manually using:
```bash
pytest -v --html=reports/report.html --self-contained-html
```

---

## ⚙️ Configuration Properties

Adjust framework attributes dynamically inside the [config.py](file:///d:/Python%20Projects/PlaywrightWebAutomation/config.py) file:

```python
class PlaywrightConfig:
    BASE_URL = "https://www.saucedemo.com/"
    HEADLESS = True               # Run browser headlessly
    VIEWPORT = {                  # Browser window dimensions
        "width": 1920,
        "height": 1080
    }
    TIMEOUT = 30000               # Selector timeout (ms)
    SLOW_MO = 500                 # Delay between actions (ms)
    SCREENSHOT = "only-on-failure" # Auto capture screenshots on failure
    VIDEO = "retain-on-failure"   # Auto record video on failure
    TRACE = "retain-on-failure"   # Record Playwright traces on failure
```

---

## 📊 Reporting & Hooks

This framework automatically utilizes the `pytest_sessionfinish` hook located in [conftest.py](file:///d:/Python%20Projects/PlaywrightWebAutomation/conftest.py). Once all test scenarios finish executing:
1.  An HTML report is generated inside the `reports/` folder.
2.  The framework locates and opens this report (`reports/report.html`) in your default web browser automatically.

---

## 🧑‍💻 Author & Contributions

Created and maintained by **Bhushan Trivedi**.
Feel free to open issues or submit pull requests for framework enhancements!
