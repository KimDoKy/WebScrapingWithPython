from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.PhantomJS()
driver.get("http://pythonscraping.com/pages/files/form.html")

firstnameField = driver.find_element_by_name("firstname")
lastnameField = driver.find_element_by_name("lastname")
submitButton = driver.find_element_by_id("submit")

### 방법 1 ###
firstnameField.send_keys("Doky")
lastnameField.send_keys("Kim")
submitButton.click()
#############

### 방법 2 ###
actions = ActionChains(driver).click(firstnameField).send_keys("Doky").click(lastnameField).send_keys("Kim").send_keys(Keys.RETURN)
actions.perform()
#############

print(driver.find_element_by_tag_name("body").text)

driver.close()
