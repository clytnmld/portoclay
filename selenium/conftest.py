import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Initialize WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    # Quit WebDriver after the test
    driver.quit()
