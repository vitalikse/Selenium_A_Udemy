import time

import pytest
from selenium.webdriver.common.by import By


class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        # time.sleep(2)
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        # time.sleep(2)
        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        # time.sleep(2)
        username_locator.send_keys(username)
        # Type password incorrectPassword into Password field
        password_locator = driver.find_element(By.NAME, "password")
        # time.sleep(2)
        password_locator.send_keys(password)
        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        # time.sleep(2)
        submit_button_locator.click()
        time.sleep(2)

        error_text = driver.find_element(By.ID, "error")
        print(error_text.text)
        assert error_text.is_displayed() and error_text.text == expected_error_message

    def test_negative_username(self, driver):
        # time.sleep(2)
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        # time.sleep(2)
        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        # time.sleep(2)
        username_locator.send_keys("incorrectUser")
        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        # time.sleep(2)
        password_locator.send_keys("Password123")
        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        # time.sleep(2)
        submit_button_locator.click()
        time.sleep(2)

        error_text = driver.find_element(By.ID, "error")
        print(error_text.text)
        assert error_text.is_displayed() and error_text.text == 'Your username is invalid!'

    def test_negative_password(self, driver):
        # time.sleep(2)
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        # time.sleep(2)
        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        # time.sleep(2)
        username_locator.send_keys("student")
        # Type password incorrectPassword into Password field
        password_locator = driver.find_element(By.NAME, "password")
        # time.sleep(2)
        password_locator.send_keys("incorrectPassword")
        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        # time.sleep(2)
        submit_button_locator.click()
        time.sleep(2)

        error_text = driver.find_element(By.ID, "error")
        print(error_text.text)
        assert error_text.is_displayed() and error_text.text == 'Your password is invalid!'
# Open page
# Type username incorrectUser into Username field
# Type password Password123 into Password field
# Push Submit button
# Verify error message is displayed
# Verify error message text is Your username is invalid!
