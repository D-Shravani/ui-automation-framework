def test_alert(driver):

    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    driver.find_element("xpath", "//button[text()='Click for JS Alert']").click()

    alert = driver.switch_to.alert

    alert.accept()

    assert "You successfully clicked an alert" in driver.page_source
def test_frame(driver):

    driver.get("https://the-internet.herokuapp.com/iframe")

    driver.switch_to.frame("mce_0_ifr")

    editor = driver.find_element("id", "tinymce")

    assert editor.is_displayed()
def test_multiple_tabs(driver):

    driver.get("https://the-internet.herokuapp.com/windows")

    driver.find_element("link text", "Click Here").click()

    tabs = driver.window_handles

    driver.switch_to.window(tabs[1])

    assert "New Window" in driver.page_source
