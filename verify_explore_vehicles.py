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

assert all_jeep, "No <h4> element contains a brand other than Jeep"

driver.quit()
