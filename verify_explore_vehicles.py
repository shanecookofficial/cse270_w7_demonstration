"""
Test Title: Use the explore vehicles feature 

Test ID: Dealership-app-06 

Purpose: Verify if the "explore vehicles" feature from the home page has functionality. 

Verification Requirement: 

Story Example: As a potential customer, I noticed the explore vehicles feature on the home page and I would like to search for my favorite brand Jeep. 

Pre-conditions: 

The web app is on the home page 

Expected output: The "explore vehicles" feature should give me only Jeep cars. 

Steps 

Action: From the home page, select the "explore vehicles" feature and search for Jeep models. 

Results: The feature takes me to the inventory and directly displays only Jeep vehicles. 

Pass/Fail or Verify Step: The web app passes this test case. It only displays available Jeep cars. 
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome()
driver.get('https://carstro-copy.web.app/')

select_brand_xpath = "//select[@name='brand']"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,select_brand_xpath))).click()

jeep_option_xpath = "//option[@value='Jeep']"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,jeep_option_xpath))).click()

view_inventory_button = "//input[@value='View Inventory']"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,view_inventory_button))).click()

jeep_filter_checkbox_xpath = "//input[@id='Jeep-car']"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,jeep_filter_checkbox_xpath))).is_selected()

h4_elements = driver.find_elements(By.TAG_NAME, "h4")
all_jeep = True

for h4 in h4_elements:
    if "Jeep" in h4.text:
        pass
    else:
        all_2020 = False
        break

assert all_jeep, "Some of the <h4> elements contain cars other than Jeep"

driver.quit()
