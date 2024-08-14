# tests/test_login.py
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import *

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://stellarburgers.nomoreparties.site/')

    def test_login_main_button(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, LOGIN_MAIN_BUTTON).click()

    def test_login_profile_button(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, LOGIN_PROFILE_BUTTON).click()

    def test_login_register_form_button(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, LOGIN_REGISTER_FORM_BUTTON).click()

    def test_login_password_recovery_button(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, LOGIN_PASSWORD_RECOVERY_BUTTON).click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

