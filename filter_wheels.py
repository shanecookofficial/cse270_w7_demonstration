"""
Test Title: Display 16" Wheels 

Test ID: Dealership-app-04 

Purpose: Filter 16" Wheels car models 

Verification Requirement: 

Story Example: As a potential customer, I would like to see cars that match my preferences (16" Wheels). 

Pre-conditions: 

The web app is on the inventory feature 

There is no filter selected 

Expected output: The web app only displays cars with the given preferences.  

Steps 

Action: From the inventory page, scroll down until the wheels filter and select the 16" Wheels box. 

Results: It only displays cars with my preference (16" Wheels). 

Pass/Fail or Verify Step: The web app passes this test case. It displays the available cars that have 16" Wheels. 
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome()
driver.get('https://carstro-copy.web.app/inventory?minPrice=4200&maxPrice=420000&minMileage=465&maxMileage=240834')

size_16_wheels_checkbox_xpath = "//input[@value='16']"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, size_16_wheels_checkbox_xpath))).click()

WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='carInventory false false']")))

# IDK why the wait doesn't work
time.sleep(2)
cars = driver.find_elements(By.XPATH, "//div[@class='carInventory false false']")
all_16 = True
for car in cars:
    try:
        third_p_tag = car.find_elements(By.TAG_NAME, "p")[2]
        
        if "16\" wheels" not in third_p_tag.text:
            all_16 = False
            break
    except IndexError:
        all_16 = False
        break

assert all_16, "Not all cars have 16\" wheels."

driver.quit()