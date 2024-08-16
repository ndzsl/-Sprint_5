from selenium.webdriver.common.by import By
from locators import *

def test_login_main_button(driver):
    driver.find_element(By.CSS_SELECTOR, LOGIN_MAIN_BUTTON).click()

def test_login_profile_button(driver):
    driver.find_element(By.CSS_SELECTOR, LOGIN_PROFILE_BUTTON).click()

def test_login_register_form_button(driver):
    driver.find_element(By.CSS_SELECTOR, LOGIN_REGISTER_FORM_BUTTON).click()

def test_login_password_recovery_button(driver):
    driver.find_element(By.CSS_SELECTOR, LOGIN_PASSWORD_RECOVERY_BUTTON).click()
