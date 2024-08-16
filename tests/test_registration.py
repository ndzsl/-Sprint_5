from selenium.webdriver.common.by import By
from locators import *

def test_successful_registration(driver):
    driver.find_element(By.CSS_SELECTOR, REGISTER_NAME_FIELD).send_keys('Надежда Планидина')
    driver.find_element(By.CSS_SELECTOR, REGISTER_EMAIL_FIELD).send_keys('nadya_planidina_9_753@example.com')
    driver.find_element(By.CSS_SELECTOR, REGISTER_PASSWORD_FIELD).send_keys('password123')
    driver.find_element(By.CSS_SELECTOR, REGISTER_SUBMIT_BUTTON).click()

def test_incorrect_password_error(driver):
    driver.find_element(By.CSS_SELECTOR, REGISTER_NAME_FIELD).send_keys('Надежда Планидина')
    driver.find_element(By.CSS_SELECTOR, REGISTER_EMAIL_FIELD).send_keys('nadya_planidina_9_753@example.com')
    driver.find_element(By.CSS_SELECTOR, REGISTER_PASSWORD_FIELD).send_keys('123')
    driver.find_element(By.CSS_SELECTOR, REGISTER_SUBMIT_BUTTON).click()
