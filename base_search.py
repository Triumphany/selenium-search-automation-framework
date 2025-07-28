from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

serv_obbj = Service('chrome_driver_pathway')
driver = webdriver.Chrome(service=serv_obbj)

driver.get("https://duckduckgo.com/")
search_input = driver.find_element(By.XPATH, "//input[@name='q']")
search_input.clear()
search_input.send_keys("selenium")
search_button = driver.find_element(By.XPATH, "//button[@type='submit']")
search_button.click()

driver.quit()