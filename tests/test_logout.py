# tests/test_logout.py
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import *

class TestLogout(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://stellarburgers.nomoreparties.site/')

    def test_logout(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, LOGIN_PROFILE_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, LOGOUT_BUTTON).click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
