from selenium.webdriver.common.by import By
from locators import *

def test_profile_menu_navigation(driver):
    driver.find_element(By.CSS_SELECTOR, PROFILE_MENU).click()

def test_constructor_navigation(driver):
    driver.find_element(By.CSS_SELECTOR, CONSTRUCTOR_BUTTON).click()

def test_logo_navigation(driver):
    driver.find_element(By.CSS_SELECTOR, LOGO_BUTTON).click()

