from selenium import webdriver
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def get_driver():
    selenium_url = os.getenv("SELENIUM_URL", "http://selenium-standalone:4444/wd/hub")

    if selenium_url:
        driver = webdriver.Remote(
            command_executor=selenium_url,
            desired_capabilities=DesiredCapabilities.CHROME
        )
    else:
        driver = webdriver.Chrome()

    return driver