"""
Test Title: Testing Clear All Button on Inventory Page 

Test ID: Dealership-app-09 

Purpose: Verify that the website clears all filters when “Clear All” button is clicked 

Verification Requirement: 

Story Example: I would like to see how easy it is to filter out different brands on Inventory page 

Pre-conditions: 

The Inventory page is selected 

One or more brands of cars are checked 

Expected output: The “View Inventory” button only displays the selected brand of vehicles 

Steps 

Action: Click on “Clear All” button 

Results: The website should display all available models once the “Clear All” button is selected 

Pass/Fail or Verify Step: The web app passes this test case. The clear all button works.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get('https://carstro-copy.web.app/inventory?minPrice=4200&maxPrice=420000&minMileage=465&maxMileage=240834')

bmw_brand_checkbox_xpath = "//input[@id='BMW-car']"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,bmw_brand_checkbox_xpath))).click()

volvo_brand_checkbox_xpath = "//input[@id='Volvo-car']"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,volvo_brand_checkbox_xpath))).click()

clear_all_button_xpath = "//button[contains(text(),'Clear All')]"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,clear_all_button_xpath))).click()

assert not driver.find_element(By.XPATH, bmw_brand_checkbox_xpath).is_selected(), "The BMW checkbox is still selected"
assert not driver.find_element(By.XPATH, volvo_brand_checkbox_xpath).is_selected(), "The Volvo checkbox is still selected"

driver.quit()