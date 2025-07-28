from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class HomePage:  # Use CamelCase for class names (PEP8)
    search_box_xpath = "//input[@name='q']"
    search_button_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def enter_search(self, utext):
        search_loc = self.driver.find_element(By.XPATH, self.search_box_xpath)
        search_loc.clear()  # Optional: clear the box before typing
        search_loc.send_keys(utext)

    def click_search(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()
