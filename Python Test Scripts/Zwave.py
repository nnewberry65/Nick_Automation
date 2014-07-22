__author__ = 'nnewberry'


from selenium import webdriver
import time
import sys
from selenium.webdriver.common.keys import Keys
file=open("results.txt", "w")

browser = webdriver.Firefox()
browser.get ('https://betacloud.vivint.com')
time.sleep(2)
browser.find_element_by_class_name('qa-email').click()
elem = browser.find_element_by_class_name('qa-email')
elem.send_keys("nnewberry@vivint.com")
time.sleep(2)
browser.find_element_by_class_name('qa-password').click()
elem = browser.find_element_by_class_name('qa-password')
elem.send_keys("muffin")
time.sleep(2)
browser.find_element_by_class_name('qa-sign-in').click()

#Lock Control
time.sleep(2)
browser.find_element_by_class_name('qa-safety-widget').click()
time.sleep(2)
browser.find_element_by_class_name('qa-slider-55-locked').click()
time.sleep(10)
file.write("Lock locked")
browser.find_element_by_class_name('qa-slider-55-unlocked').click()
file.write("Lock unlocked")

file.close()


#Light Control
time.sleep(2)
browser.find_element_by_class_name('qa-control-widget').click()
time.sleep(2)
browser.find_element_by_class_name('qa-slider-72').click()
time.sleep(10)
browser.find_element_by_class_name('qa-slider-72-off').click()

