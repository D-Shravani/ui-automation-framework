import pytest
from pages.login_page import LoginPage


def test_valid_login(driver):

    login = LoginPage(driver)

    login.login("tomsmith", "SuperSecretPassword!")

    assert "Secure Area" in driver.page_source


@pytest.mark.parametrize("email,password", [

    ("wrong@test.com", "123"),
    ("invalidemail", "test"),
    ("", "")

])
def test_invalid_login(driver, email, password):

    login = LoginPage(driver)

    login.login(email, password)

    assert "Your username is invalid" in driver.page_source
