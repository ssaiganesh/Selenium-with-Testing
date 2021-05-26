from selenium import webdriver
# from selenium.webdriver.common.keys import Keys  # only needed when have to send_keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_location = "/usr/local/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"

options = webdriver.ChromeOptions()
options.binary_location = binary_location

driver = webdriver.Chrome(executable_path=driver_location, options=options)
driver.get("https://techwithtim.net")

# Tutorial 3
print("Finding Python Programming Link")
link = driver.find_element_by_link_text("Python Programming")
link.click()
print("Opened Python Programming link")

# Advertisements are shown
# Manually maximise this is not even needed, so question: If maximised driver from the start, this can be avoided?
driver.back()  # Go to previous page
driver.forward()  # Go to next page

try:
    print("Finding for Beginner Python Tutorials")
    element = WebDriverWait(driver, 10).until(
        # EC.presence_of_element_located((By.ID, "myDynamicElement"))
        # EC.presence_of_element_located(By.LINK_TEXT, "Beginner Python Tutorials")  # on the side menu list
        EC.presence_of_element_located((By.ID, "menu-item-511"))
    )
    element.click()
    print("In Beginner Python Tutorials Link")
except:
    print("Did not find Beginner Python tutorials")
    driver.quit()
    print("Driver Closed")

try:
    print("Finding for Get Started Button")
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )

    # element.clear() # For tutorial purpose, this means element definition is cleared
    # Can define new element if used element.clear()

    element.click()
    print("Clicked Button")
except:
    print("Did not find Button")
    driver.quit()
# driver.quit()
# print("Driver closed")

