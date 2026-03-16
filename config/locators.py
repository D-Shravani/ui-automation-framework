from selenium.webdriver.common.by import By

class LoginLocators:

    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
