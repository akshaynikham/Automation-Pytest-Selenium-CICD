# from selenium import webdriver
# from utils import get_driver

# def Initiate_driver():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(10)
#     return driver

def homepage(driver):
    driver.get("https://www.flipkart.com/")
    # driver.maximize_window()
    # driver.quit()
