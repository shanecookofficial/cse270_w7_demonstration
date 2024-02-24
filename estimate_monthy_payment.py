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

WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".carInventory_link .btn")))
first_view_details_button = driver.find_element(By.CSS_SELECTOR, ".carInventory_link .btn")
first_view_details_button.click()

car_cost_xpath = "//span[@class='carDetails_features-bigPrice']/span"
raw_car_cost = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,car_cost_xpath))).text
car_cost = int(raw_car_cost.replace("$", "").replace(",", ""))

cash_down = random.randint(0,car_cost)
principal = car_cost - cash_down
cash_down_input_xpath = "//input[@name='cashDown']"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,cash_down_input_xpath))).clear()
driver.find_element(By.XPATH,cash_down_input_xpath).send_keys(str(cash_down))

term_length_select = Select(driver.find_element(By.XPATH, "//label[contains(text(), 'Term Length')]/following-sibling::select"))
selected_term_length_option = term_length_select.first_selected_option
term = int(''.join(re.findall(r'\d+',selected_term_length_option.text)))

apr_input_xpath = "//label[contains(text(), 'Estimated APR')]/following-sibling::input"
apr_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, apr_input_xpath)))
raw_apr = apr_input.get_attribute('value')
apr = float(raw_apr.replace("%",""))

monthly_rate = (apr/100/12)
monthly_payment = str(round(principal * (monthly_rate * (1 + monthly_rate)**term) / ((1 + monthly_rate)**term - 1)))

time.sleep(3)
cost_per_month_value_xpath = "//p[@class='loanCalculator_result-price']/span/span"
assert driver.find_element(By.XPATH,cost_per_month_value_xpath).text == monthly_payment

driver.quit()