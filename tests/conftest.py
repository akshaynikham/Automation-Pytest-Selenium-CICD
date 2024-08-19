import pytest
# from selenium import webdriver
from pages.utils import get_driver

@pytest.fixture()
def initialize_driver():
    driver = get_driver()
    yield driver
    driver.quit()
