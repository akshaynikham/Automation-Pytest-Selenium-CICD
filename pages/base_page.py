from selenium import webdriver

def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    return driver

def homepage(driver=driver()):
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    driver.quit()
