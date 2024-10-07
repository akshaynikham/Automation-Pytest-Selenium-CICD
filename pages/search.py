from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class search_Select:
    def __init__(self,driver):
        self.driver = driver

    def search_items(self, ProductName):
        self.driver.get("https://www.flipkart.com/")
        main_window = self.driver.current_window_handle
        print("current window handle", main_window)
        search_box = self.driver.find_element(By.XPATH, "//input[@placeholder='Search for Products, Brands and More']")
        search_box.click()
        search_box.send_keys(ProductName)
        search_box.send_keys(Keys.RETURN)
        results = self.driver.find_elements(By.CLASS_NAME, "KzDlHZ")
        select = results[0]
        select.click()
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[1])
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.save_screenshot("first_try.png")
        # return [result.text for result in results]

class search_only:
    def __init__(self,driver):
        self.driver = driver

    def search_items(self, ProductName):
        search_box = self.driver.find_element(By.XPATH, "//input[@placeholder='Search for Products, Brands and More']")
        search_box.click()
        search_box.clear()
        search_box.send_keys(ProductName)
        search_box.send_keys(Keys.RETURN)
        results = self.driver.find_elements(By.CLASS_NAME, "KzDlHZ")