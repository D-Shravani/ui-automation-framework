from selenium import webdriver
from config.settings import GRID_URL, HEADLESS

def get_driver():

    options = webdriver.ChromeOptions()

    if HEADLESS == "true":
        options.add_argument("--headless")

    if GRID_URL:
        driver = webdriver.Remote(
            command_executor=GRID_URL,
            options=options
        )
    else:
        driver = webdriver.Chrome(options=options)

    driver.maximize_window()

    return driver
