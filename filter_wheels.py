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

# Wait for the cars to be loaded after applying the filter
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='carInventory false false']")))

# IDK why the wait doesn't work
time.sleep(2)
# Your previous code

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