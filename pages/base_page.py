from selenium import webdriver

def Initiate_driver():

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    return driver

def homepage(driver=Initiate_driver()):
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    driver.quit()
