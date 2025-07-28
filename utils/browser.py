import os
from datetime import datetime

def save_screenshot(driver, test_name):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folder = "screenshots"
    os.makedirs(folder, exist_ok=True)
    filepath = f"{folder}/{test_name}_{timestamp}.png"
    driver.save_screenshot(filepath)
    return filepath
