import os
import webbrowser
import pytest
# pyrefly: ignore [missing-import]
import allure

@pytest.fixture(scope="session", autouse=True)
def configure_playwright(playwright):
    playwright.selectors.set_test_id_attribute("data-test")

# Hook to capture screenshots on test failure and attach them to Allure report
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
    # We check if the test failed in the execution call phase
    if rep.when == "call" and rep.failed:
        # Retrieve the 'page' fixture from the test item
        page = item.funcargs.get("page")
        if page:
            try:
                screenshot_bytes = page.screenshot(full_page=True)
                allure.attach(
                    screenshot_bytes,
                    name="Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print(f"Failed to capture screenshot: {e}")

def pytest_sessionfinish(session, exitstatus):
    report_path = os.path.abspath("reports/report.html")
    if os.path.exists(report_path) and not os.environ.get("CI"):
        webbrowser.open(f"file://{report_path}")