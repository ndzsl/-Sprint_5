from selenium.webdriver.common.by import By
from locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_buns_section(driver):
    driver.find_element(By.CSS_SELECTOR, CONSTRUCTOR_BUTTON).click()
    driver.find_element(By.CSS_SELECTOR, BUNS_SECTION).click()
    buns_section_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, BUNS_SECTION))
    )
    assert buns_section_element.is_displayed()

def test_sauces_section(driver):
    driver.find_element(By.CSS_SELECTOR, CONSTRUCTOR_BUTTON).click()
    driver.find_element(By.CSS_SELECTOR, SAUCES_SECTION).click()
    sauces_section_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, SAUCES_SECTION))
    )
    assert sauces_section_element.is_displayed()

def test_fillings_section(driver):
    driver.find_element(By.CSS_SELECTOR, CONSTRUCTOR_BUTTON).click()
    driver.find_element(By.CSS_SELECTOR, FILLINGS_SECTION).click()
    fillings_section_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, FILLINGS_SECTION))
    )
    assert fillings_section_element.is_displayed()

