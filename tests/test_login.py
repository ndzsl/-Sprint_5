from selenium.webdriver.common.by import By
from locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_main_button(driver):
    driver.find_element(By.CSS_SELECTOR, LOGIN_MAIN_BUTTON).click()
    main_page_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, MAIN_PAGE_INDICATOR))
    )
    assert main_page_element.is_displayed()

def test_login_profile_button(driver):
    driver.find_element(By.CSS_SELECTOR, LOGIN_PROFILE_BUTTON).click()
    profile_page_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, PROFILE_PAGE_INDICATOR))
    )
    assert profile_page_element.is_displayed()

def test_login_register_form_button(driver):
    driver.find_element(By.CSS_SELECTOR, LOGIN_REGISTER_FORM_BUTTON).click()
    register_form_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, REGISTER_FORM_INDICATOR))
    )
    assert register_form_element.is_displayed()

def test_login_password_recovery_button(driver):
    driver.find_element(By.CSS_SELECTOR, LOGIN_PASSWORD_RECOVERY_BUTTON).click()
    password_recovery_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, PASSWORD_RECOVERY_INDICATOR))
    )
    assert password_recovery_element.is_displayed()
