from selenium.webdriver.common.by import By
from locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_logout(driver):
    driver.find_element(By.CSS_SELECTOR, LOGIN_PROFILE_BUTTON).click()
    driver.find_element(By.CSS_SELECTOR, LOGOUT_BUTTON).click()
    login_page_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, LOGIN_PAGE_INDICATOR))
    )
    assert login_page_element.is_displayed()

