# tests/test_registration.py
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import *

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://stellarburgers.nomoreparties.site/')

    def test_successful_registration(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, REGISTER_NAME_FIELD).send_keys('Надежда Планидина')
        driver.find_element(By.CSS_SELECTOR, REGISTER_EMAIL_FIELD).send_keys('nadya_planidina_9_753@example.com')
        driver.find_element(By.CSS_SELECTOR, REGISTER_PASSWORD_FIELD).send_keys('password123')
        driver.find_element(By.CSS_SELECTOR, REGISTER_SUBMIT_BUTTON).click()

    def test_incorrect_password_error(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, REGISTER_NAME_FIELD).send_keys('Надежда Планидина')
        driver.find_element(By.CSS_SELECTOR, REGISTER_EMAIL_FIELD).send_keys('nadya_planidina_9_753@example.com')
        driver.find_element(By.CSS_SELECTOR, REGISTER_PASSWORD_FIELD).send_keys('123')
        driver.find_element(By.CSS_SELECTOR, REGISTER_SUBMIT_BUTTON).click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

