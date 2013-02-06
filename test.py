from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import time

driver=webdriver.Remote("http://localhost:4444/wd/hub",DesiredCapabilities.INTERNETEXPLORER)

# go to the google home page
driver.get("http://www.baidu.com")

# find the element that's name attribute is q (the google search box)
#inputElement = driver.find_element_by_name("q")

# type in the search
#inputElement.send_keys("Cheese!")

# submit the form (although google automatically searches now without submitting)
#inputElement.submit()

# the page is ajaxy so the title is originally this:
print driver.title
time.sleep(1)  
driver.find_element_by_xpath("//input[@id='kw']").clear()  
driver.find_element_by_xpath("//input[@id='kw']").send_keys("testMiaozhen")  
driver.find_element_by_xpath("//input[@id='su']").click()  
time.sleep(1)  
try:

    print driver.title

finally:
    driver.quit()

