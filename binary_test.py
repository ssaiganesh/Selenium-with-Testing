#! /usr/bin/python3

from selenium import webdriver
import time
driver_location = "/usr/local/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"

options = webdriver.ChromeOptions()
options.binary_location = binary_location

driver = webdriver.Chrome(executable_path = driver_location, options = options)
driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title) # returns the title of the page
print(driver.current_url) # returns the current url of the page

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(5)

driver.close()
