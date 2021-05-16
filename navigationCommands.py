#! /usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver_location = "/usr/local/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"
options = webdriver.ChromeOptions()
options.binary_location = binary_location
driver = webdriver.Chrome(executable_path=driver_location, options=options)

driver.get("http://www.google.com/")

print(driver.title)  # First

driver.get("http://pavantestingtools.blogspot.in/")

time.sleep(5)

print(driver.title)  # Second

driver.back()

time.sleep(5)

print(driver.title)  # First

driver.forward()

time.sleep(5)

print(driver.title)  # Second

