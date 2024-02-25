"""
Test Title: Display BMW 2020 models 

Test ID: Dealership-app-01 

Purpose: Filter and display only BMW 2020 models from the inventory feature 

Verification Requirement: 

Story Example: As a potential customer, I would like to see the availability of BMW 2020 models. 

Pre-conditions: 

The web app is on the inventory feature 

There is no filter selected 

Expected output: The web app should only display BMW 2020 models available in a friendly way. 

Steps 

Action: From the inventory page, hit the BMW box to access only that brand. 

Results: The inventory is only displaying BMW cars now. 

Action: From the filter section of the inventory, scroll down until the model year and hit the 2020 box to display only BMW 2020 models.  

Results: The web app is only displaying the three BMW 2020 models available. 

Pass/Fail or Verify Step: The web app passes this test case. It displays the selected brand and model year requested in a friendly and easy way.  
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get('https://carstro-copy.web.app/inventory?minPrice=4200&maxPrice=420000&minMileage=465&maxMileage=240834')

bmw_box_xpath = "//input[@id='BMW-car']"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,bmw_box_xpath))).click()

year_2020_box_xpath = "//input[@id='2020-car']"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,year_2020_box_xpath))).click()

# IDK why the wait doesn't work
time.sleep(2)
h4_elements = driver.find_elements(By.TAG_NAME, "h4")
all_2020 = True

for h4 in h4_elements:
    if "2020" in h4.text:
        pass
    else:
        all_2020 = False
        break

assert all_2020, "No <h4> element contains a year other than 2020"


driver.quit()