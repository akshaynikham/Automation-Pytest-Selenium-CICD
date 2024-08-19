from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def search_items(driver):
    driver.get("https://www.flipkart.com/")
    search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search for Products, Brands and More']")
    search_box.click()
    search_box.send_keys("mobile")
    search_box.send_keys(Keys.RETURN)
