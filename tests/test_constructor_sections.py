# tests/test_constructor_sections.py
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import *

class TestConstructorSections(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://stellarburgers.nomoreparties.site/')

    def test_buns_section(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, CONSTRUCTOR_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, BUNS_SECTION).click()

    def test_sauces_section(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, CONSTRUCTOR_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, SAUCES_SECTION).click()

    def test_fillings_section(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, CONSTRUCTOR_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, FILLINGS_SECTION).click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
