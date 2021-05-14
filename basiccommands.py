from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

### CHROME
#CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'  -- this is default for all drivers
WINDOW_SIZE = "1920,1080"
opts = Options()
opts.add_argument("--headless")
opts.add_argument("--window-size=%s" % WINDOW_SIZE)
opts.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=opts)

driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title) # returns the title of the page

print(driver.current_url) # returns the URL of the page

#print(driver.page_source) # HTML code for the page

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

time.sleep(5)


driver.close() # closes inital tab open

driver.quit() # closes full browser


