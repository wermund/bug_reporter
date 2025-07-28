import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime 

URL = "https://the-internet.herokuapp.com/login"

def test_invalid_login(setup_browser):
    driver = setup_browser
    driver.get(URL)

    driver.find_element(By.ID, "username").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    wait = WebDriverWait(driver, 5)
    error = wait.until(EC.visibility_of_element_located((By.ID, "flash"))).text

    try:
        assert "Your username is invalid!" in error
    except AssertionError as e:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = f"screenshots/bug_login_{timestamp}.png"
        markdown_path = f"reports/bug_login_{timestamp}.md"

        driver.save_screenshot(screenshot_path)

        with open(markdown_path, "w") as f:
            f.write(f"# ❌ Bug Report — Login Test\n\n")
            f.write(f"**Timestamp:** {timestamp}\n\n")
            f.write(f"**Error Message:** {str(e)}\n\n")
            f.write(f"**Screenshot:** ![]({screenshot_path})\n")

        raise e
