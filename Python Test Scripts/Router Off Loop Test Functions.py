from selenium import webdriver
import time


browser = webdriver.Firefox()
browser.get ('http://192.168.0.1')

#Login to the main page of the router admin screen
def login():
    browser.find_element_by_name('login').click()
    browser.get ('http://192.168.0.1/wizard_wireless.asp')
    return;

#Toggle on/off wireless broadcast on router
def wirelessswitch():
    browser.find_element_by_name('wizard').click()
    browser.find_element_by_name('w_enable').click()
    time.sleep(5)
    browser.find_element_by_name('button').click()
    time.sleep(5)
    browser.find_element_by_name('reboot').click()
    time.sleep(80)
    return;


count = 0
while (count < 10):
    login();
    wirelessswitch();
    login();
    wirelessswitch();
    browser.get ('http://192.168.0.1')
    count = count + 1
    



