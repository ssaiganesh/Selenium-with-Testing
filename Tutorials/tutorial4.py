from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver_location = "/usr/local/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"

options = webdriver.ChromeOptions()
options.binary_location = binary_location

driver = webdriver.Chrome(executable_path=driver_location, options=options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)  # Due to Loading Page therefore had error for not being able to find elements

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")

items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]

actions = ActionChains(driver)
actions.click(cookie)
actions.perform()

for i in range(5000):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0].replace(",", ""))  # replace commas for thousands
    for item in items:
        value = int(item.text.replace(",", ""))
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()







