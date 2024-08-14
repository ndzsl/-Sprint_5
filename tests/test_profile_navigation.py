# tests/test_profile_navigation.py
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import *

class TestProfileNavigation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://stellarburgers.nomoreparties.site/')

    def test_profile_menu_navigation(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, PROFILE_MENU).click()

    def test_constructor_navigation(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, CONSTRUCTOR_BUTTON).click()

    def test_logo_navigation(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, LOGO_BUTTON).click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
