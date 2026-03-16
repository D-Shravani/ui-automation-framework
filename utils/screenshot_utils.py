import os

def capture_screenshot(driver, name):

    path = f"reports/{name}.png"

    driver.save_screenshot(path)
