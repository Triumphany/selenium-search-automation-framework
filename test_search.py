import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.dirname(__file__))

from home_page import HomePage

class TestSearch:

    def setup_method(self):
        serv_obj = Service("Chrom_driver_pathway")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.get("https://duckduckgo.com/")

    def teardown_method(self):
        self.driver.quit()

    def test_search_text(self):  
        search_w = HomePage(self.driver)  
        search_w.enter_search("selenium")
        search_w.click_search()

    def test_search_number(self):
        search_w = HomePage(self.driver) 
        search_w.enter_search("1")
        search_w.click_search()

    



