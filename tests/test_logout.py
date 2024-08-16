from selenium.webdriver.common.by import By
from locators import *
def test_logout(driver):
    driver.find_element(By.CSS_SELECTOR, LOGIN_PROFILE_BUTTON).click()
    driver.find_element(By.CSS_SELECTOR, LOGOUT_BUTTON).click()
