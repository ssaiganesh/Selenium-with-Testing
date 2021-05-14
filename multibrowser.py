#
#
#
#

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import FirefoxOptions

### CHROME
#CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'  -- this is default for all drivers
WINDOW_SIZE = "1920,1080"
opts = Options()
opts.add_argument("--headless")
opts.add_argument("--window-size=%s" % WINDOW_SIZE)
opts.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=opts)


### FIREFOX
"""
#from selenium.webdriver.common.keys import Keys

opts = FirefoxOptions()
opts.add_argument("--headless")
driver = webdriver.Firefox(options=opts)
"""
driver.get("https://www.google.com/")

print(driver.title) # Title of the page

print(driver.current_url) # returns the URL of the page

#print(driver.page_source) # HTML code for the page

#driver.close() #Close the browser



