import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():

    grid_url = os.getenv("GRID_URL", "http://localhost:4444/wd/hub")

    chrome_options = Options()

    driver = webdriver.Remote(
        command_executor=grid_url,
        options=chrome_options
    )

    driver.maximize_window()

    yield driver

    driver.quit()

