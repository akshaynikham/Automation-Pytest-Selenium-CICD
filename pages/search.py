from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class flipkartSearch:
    def __init__(self,driver):
        self.driver = driver

    def search_items(self, ProductName):
        self.driver.get("https://www.flipkart.com/")
        search_box = self.driver.find_element(By.XPATH, "//input[@placeholder='Search for Products, Brands and More']")
        search_box.click()
        search_box.send_keys(ProductName)
        search_box.send_keys(Keys.RETURN)
        results = self.driver.find_elements(By.CLASS_NAME, "KzDlHZ")
        return [result.text for result in results]

