"""
Test Title: Contact a sales representative  

Test ID: Dealership-app-03 

Purpose: Contact a sales representative and send a message through the web application. 

Verification Requirement: 

Story Example: As a potential customer, I would like to contact and get more information about a specific car. 

Pre-conditions: 

The web app is on the sales representatives feature 

Salt Lake City is the chosen location and representative 

Expected output: The web app should let me text the representative and display a friendly message when I send my message.  

Steps 

Action: In the sales representatives page, click on Salt Lake City location and select “contact dealer”. 

Results: It prompts for personal info to contact me and displays a box of text where I can write my message. 

Action: Provide my information and send a message to the dealer. 

Results: It displays “message sent”. 

Pass/Fail or Verify Step: The web app passes this test case. The contact dealer feature works, and I can send messages through the web app.  
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import names
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get('https://carstro-copy.web.app/salesRepresentatives')

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "salesRepresentatives_ul")))

salt_lake_rep = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((
        By.XPATH,
        "//p[contains(text(), 'Salt Lake, UT')]/ancestor::li"
    ))
)
salt_lake_rep.click()

salt_lake_section = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//ul/li[contains(.,'Salt Lake, UT')]")))

contact_dealer_button = salt_lake_section.find_element(By.XPATH, ".//button[contains(text(), 'Contact Dealer')]")
contact_dealer_button.click()

name_xpath = "//input[@placeholder='Name']"
random_fname = names.get_first_name()
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,name_xpath))).send_keys(random_fname)

last_name_xpath = "//input[@placeholder='Last Name']"
random_lname = names.get_last_name()
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,last_name_xpath))).send_keys(random_lname)

email_xpath = "//input[@placeholder='Email']"
email = random_fname+"."+random_lname+"@gmail.com"
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,email_xpath))).send_keys(email)

comment_xpath = "//*[@name='comment']"
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,comment_xpath))).send_keys("Keep up the great work :)")

contact_dealer_button_xpath = "//button[contains(text(),'Contact Dealer')]"
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,contact_dealer_button_xpath))).click()

try:
    modal_confirmation_xpath = "//div[@class='modal_confirmation']"
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,modal_confirmation_xpath)))
    assert True
except NoSuchElementException:
    assert False, "Message Sent modal is not present"

driver.quit()