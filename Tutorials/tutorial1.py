from selenium import webdriver

driver_location = "/usr/local/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"

options = webdriver.ChromeOptions()
options.binary_location = binary_location

driver = webdriver.Chrome(executable_path=driver_location, options=options)
driver.get("https://techwithtim.net")
print(driver.title)  # prints the page title
driver.close()  # close the current tab
driver.quit()  # closes entire browser
