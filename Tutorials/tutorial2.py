# Most common ways to access element:
# id -- guaranteed to be unique
# name -- not necessarily unique but usually is
# class -- returns first element it finds and not necessarily unique

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import time  # Module not needed due to explicit wait

driver_location = "/usr/local/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"

options = webdriver.ChromeOptions()
options.binary_location = binary_location

driver = webdriver.Chrome(executable_path=driver_location, options=options)
driver.get("https://techwithtim.net")

search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)  # same as ENTER -- double check on this

# print(driver.page_source)  # scrapes and access source code for entire website not that useful

# main = driver.find_element_by_id("main")  -- may give error if not loaded in time hence the explicit wait below

"""
Explicit Wait 

An explicit wait is a code you define to wait for a certain condition to 
occur before proceeding further in the code. The extreme case of this is 
time.sleep(), which sets the condition to an exact time period to wait. 
There are some convenience methods provided that help you write code that 
will wait only as long as required. WebDriverWait in combination with 
ExpectedCondition is one way this can be accomplished.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://somedomain/url_that_delays_loading")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally: # quit no matter if try works or not .. 
    driver.quit()
"""

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    # print(main.text)
    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        # header = article.find_element_by_class_name("entry-title")  #h1 tag
        # -- printing this returns blank same as how we cannot see any header in the page

        header = article.find_element_by_class_name("entry-summary")
        print(header.text)
finally:
    # time.sleep(5) # replaced by explicit wait
    driver.quit()  # closes entire browser
"""
except:
    # except means to quit only if try doesn't work
    driver.quit()
"""




