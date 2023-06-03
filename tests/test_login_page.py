# def print_hi(name):
#     print(f"Hi, {name}")
#
# if __name__ == "__main__":
#     print_hi("Vitaly")
# Open browser
import time

import pytest
from selenium.webdriver.common.by import By


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        time.sleep(2)
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)
        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        time.sleep(2)
        username_locator.send_keys("student")
        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        time.sleep(2)
        password_locator.send_keys("Password123")
        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        time.sleep(2)
        submit_button_locator.click()
        time.sleep(2)

        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        actual_url = driver.current_url
        print(actual_url)
        assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

        # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        expected_text = driver.find_element(By.CLASS_NAME, "post-content")
        expected_text = driver.find_element(By.TAG_NAME, "h1")
        actual_text = expected_text.text
        print(actual_text)
        assert actual_text == "Logged In Successfully"

        # Verify button Log out is displayed on the new page
        log_out_button = driver.find_element(By.XPATH, "//a[text()='Log out']")
        log_out_button = driver.find_element(By.LINK_TEXT, "Log out")

        assert log_out_button.is_displayed()
