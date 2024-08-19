from selenium.webdriver.common.by import By
from locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_successful_registration(driver):
    driver.find_element(By.CSS_SELECTOR, REGISTER_NAME_FIELD).send_keys('Надежда Планидина')
    driver.find_element(By.CSS_SELECTOR, REGISTER_EMAIL_FIELD).send_keys('nadya_planidina_9_753@example.com')
    driver.find_element(By.CSS_SELECTOR, REGISTER_PASSWORD_FIELD).send_keys('password123')
    driver.find_element(By.CSS_SELECTOR, REGISTER_SUBMIT_BUTTON).click()
    success_message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, SUCCESS_MESSAGE_INDICATOR))
    )
    assert success_message_element.is_displayed()

def test_incorrect_password_error(driver):
    driver.find_element(By.CSS_SELECTOR, REGISTER_NAME_FIELD).send_keys('Надежда Планидина')
    driver.find_element(By.CSS_SELECTOR, REGISTER_EMAIL_FIELD).send_keys('nadya_planidina_9_753@example.com')
    driver.find_element(By.CSS_SELECTOR, REGISTER_PASSWORD_FIELD).send_keys('123')
    driver.find_element(By.CSS_SELECTOR, REGISTER_SUBMIT_BUTTON).click()
    error_message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ERROR_MESSAGE_INDICATOR))
    )
    assert error_message_element.is_displayed()
