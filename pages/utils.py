from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def get_driver():
    selenium_url = os.getenv("SELENIUM_URL", "http://localhost:4444/wd/hub")

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Update `webdriver.Remote` without `desired_capabilities`
    driver = webdriver.Remote(
        command_executor=selenium_url,
        options=chrome_options
    )
    return driver





# from selenium import webdriver
# import os
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.chrome.options import Options
#
# def get_driver():
#     selenium_url = os.getenv("SELENIUM_URL", "http://localhost:4444/wd/hub")
#
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#
#     if selenium_url:
#         driver = webdriver.Remote(
#             command_executor=selenium_url,
#             desired_capabilities=DesiredCapabilities.CHROME,
#             options=chrome_options
#         )
#     else:
#         driver = webdriver.Chrome(options=chrome_options)
#
#     return driver