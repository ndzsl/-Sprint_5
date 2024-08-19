from selenium.webdriver.common.by import By
from locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_profile_menu_navigation(driver):
    driver.find_element(By.CSS_SELECTOR, PROFILE_MENU).click()
    profile_page_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, PROFILE_PAGE_INDICATOR))
    )
    assert profile_page_element.is_displayed()

def test_constructor_navigation(driver):
    driver.find_element(By.CSS_SELECTOR, CONSTRUCTOR_BUTTON).click()
    constructor_page_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, CONSTRUCTOR_PAGE_INDICATOR))
    )
    assert constructor_page_element.is_displayed()

def test_logo_navigation(driver):
    driver.find_element(By.CSS_SELECTOR, LOGO_BUTTON).click()
    home_page_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, HOME_PAGE_INDICATOR))
    )
    assert home_page_element.is_displayed()


