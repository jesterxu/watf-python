#coding: utf-8
import time
from Data.Kace.page.iKace import iKace



def setup(mlog,driver):
    driver.get(iKace.iUrl)
    driver.maximize_window()  
    
def test(mlog,driver):       

    print driver.title
    time.sleep(1)  
    driver.find_element_by_xpath(iKace.inputfield).clear()  
    driver.find_element_by_xpath(iKace.inputfield).send_keys("jesterxu")  
    driver.find_element_by_xpath(iKace.searchPB).click() 
    driver.find_element_by_xpath(iKace.firstlink).click() 
    time.sleep(5)  

    print driver.title       
    
def teardown(mlog,driver):
    return