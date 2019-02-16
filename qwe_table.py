from selenium import webdriver
#from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.get('file:///G:/selinium/qwebtable.html')
driver.maximize_window()
driver.implicitly_wait(10)
element=driver.find_elements_by_xpath('//*[@id="emp"]/thead/tr/th')
print(len(element))
first_part='//*[@id="emp"]/tbody/tr[1]/td'
second_part='//*[@id="emp"]/tbody/tr[2]/td'
