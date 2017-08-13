from selenium import webdriver
import time

driver = webdriver.PhantomJS()
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)
print(driver.find_elements_by_css_selector("#content")[0].text)
# print(driver.find_elements_by_css_selector("div"))
driver.close()
