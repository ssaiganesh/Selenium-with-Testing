#! /usr/bin/python3

from selenium import webdriver

driver_location = "/usr/local/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"

options = webdriver.ChromeOptions()
options.binary_location = binary_location

driver = webdriver.Chrome(executable_path=driver_location, options=options)
driver.get("http://automationpractice.com/index.php/")

sign_in = driver.find_element_by_class_name("login")
sign_in.click()

email_ele = driver.find_element_by_name("email")

print(email_ele.is_displayed())  # returns true/false based on element status
print(email_ele.is_enabled())  # returns true/false

"""
is_displayed is used to verify presence of web element within webpage

is_enabled is the method used to verify if web element is enabled or disabled
Primarily used with buttons

is_selected is the method used to verify if the web element is selected or not
predominantly used with radio buttons, dropdowns, and checkboxes
"""



