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