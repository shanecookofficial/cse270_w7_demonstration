from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import re
import random


driver = webdriver.Chrome()
driver.get('https://carstro-copy.web.app/inventory?minPrice=4200&maxPrice=420000&minMileage=465&maxMileage=240834')

bmw_brand_checkbox_xpath = "//input[@id='BMW-car']"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,bmw_brand_checkbox_xpath))).click()

volvo_brand_checkbox_xpath = "//input[@id='Volvo-car']"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,volvo_brand_checkbox_xpath))).click()

clear_all_button_xpath = "//button[contains(text(),'Clear All')]"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,clear_all_button_xpath))).click()

assert not driver.find_element(By.XPATH, bmw_brand_checkbox_xpath).is_selected()
assert not driver.find_element(By.XPATH, volvo_brand_checkbox_xpath).is_selected()

driver.quit()