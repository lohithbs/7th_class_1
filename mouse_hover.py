from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
print(driver)
driver.get('https://www.flipkart.com/')
driver.maximize_window()
driver.implicitly_wait(10)
element=driver.find_elements_by_xpath("//span[text()='Men']")
hover=ActionChains(driver).move_to_element(element)
hover.perform()
