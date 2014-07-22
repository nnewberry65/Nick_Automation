from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get ('http://192.168.0.1')


#Outbound Traffic Block
browser.get ('http://http://192.168.0.1/adv_access_control.asp')
browser.find_element_by_name('access_enable').click()
if browser.get_attribute = "true":
    browser.find_element_by_name('button').click()
    time.sleep(5)
    browser.find_element_by_name('reboot').click()
    time.sleep(80)
else:
    browser.find_element_by_name('enable0').click()
    browser.find_element_by_name('button').click()
    time.sleep(5)
    browser.find_element_by_name('reboot').click()
    time.sleep(80)
    
                                        
