import os
import webbrowser
import pytest

@pytest.fixture(scope="session", autouse=True)
def configure_playwright(playwright):
    playwright.selectors.set_test_id_attribute("data-test")

def pytest_sessionfinish(session, exitstatus):
    report_path = os.path.abspath("reports/report.html")
    if os.path.exists(report_path):
        webbrowser.open(f"file://{report_path}")