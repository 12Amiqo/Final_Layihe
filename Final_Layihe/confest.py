import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()  # Ensure you have the correct driver for your browser
    yield driver
    driver.quit()
