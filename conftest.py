import pytest
from selenium import webdriver
from utils.browser import save_screenshot
from utils.reporter import generate_markdown_report

@pytest.fixture
def setup_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def pytest_exception_interact(node, call, report):
    if report.failed and "setup_browser" in node.fixturenames:
        driver = node.funcargs["setup_browser"]
        test_name = node.nodeid
        screenshot_path = save_screenshot(driver, test_name)
        error_message = str(call.excinfo.value)
        generate_markdown_report(test_name, error_message, screenshot_path)

