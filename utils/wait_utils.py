from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(driver, locator, time=10):

    wait = WebDriverWait(driver, time)

    return wait.until(
        EC.visibility_of_element_located(locator)
    )
