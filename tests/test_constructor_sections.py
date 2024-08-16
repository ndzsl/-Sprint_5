from selenium.webdriver.common.by import By
from locators import *

def test_buns_section(driver):
    driver.find_element(By.CSS_SELECTOR, CONSTRUCTOR_BUTTON).click()
    driver.find_element(By.CSS_SELECTOR, BUNS_SECTION).click()

def test_sauces_section(driver):
    driver.find_element(By.CSS_SELECTOR, CONSTRUCTOR_BUTTON).click()
    driver.find_element(By.CSS_SELECTOR, SAUCES_SECTION).click()

def test_fillings_section(driver):
    driver.find_element(By.CSS_SELECTOR, CONSTRUCTOR_BUTTON).click()
    driver.find_element(By.CSS_SELECTOR, FILLINGS_SECTION).click()
