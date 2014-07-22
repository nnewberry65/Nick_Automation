from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get ('http://192.168.0.1')

#Login to the main page of the router admin screen
def login():
    browser.find_element_by_name('login').click()
    browser.get ('http://192.168.0.1/wizard_wireless.asp')
    return;

#Login to the Router Settings of the router admin screen
def routersettings():
    browser.find_element_by_name('login').click()
    browser.get ('http://192.168.0.1/lan')
    return;

#Select Manual Wireless Button From Wireless Menu
def manualwireless():
    browser.find_element_by_name('wizard').click()
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

#Toggle on/off Wireless Visibility
def wirelessvisibility():
    browser.find_element_by_name('wlan0_ssid_broadcast').click()
    browser.find_element_by_name('wizard').click()
    browser.find_element_by_name('w_enable').click()
    time.sleep(5)
    browser.find_element_by_name('button').click()
    time.sleep(5)
    browser.find_element_by_name('reboot').click()
    time.sleep(80)
    return;

#Change the SSID name
def SSIDname():
    browser.find_element_by_name('show_ssid').click()
    elem = browser.find_element_by_name('show_ssid')
    elem.clear()
    elem.send_keys("ssidname")

#Change the SSID password
def SSIDpassword():
    browser.find_element_by_name('wlan0_psk_pass_phrase').click()
    elem = browser.find_element_by_name('wlan0_psk_pass_phrase')
    elem.clear()
    elem.send_keys("password")

#Toggle on/off Auto Channel
def AutoChannel():
    browser.find_element_by_name('auto_channel').click()
    return;

#Change Security Mode to WPA
def securitymodedropdown_WPA():
    browser.find_element_by_name('wep_type').click()
    elem = browser.find_element_by_name('wep_type')
    elem.send_keys(Keys.ARROW_UP)
    elem.send_keys(Keys.ARROW_UP)
    elem.send_keys(Keys.ARROW_UP)
    elem.send_keys(Keys.ARROW_DOWN)
    elem.send_keys(Keys.ARROW_DOWN)
    elem.send_keys(Keys.ENTER)
    return;

#Change Security Mode to None
def securitymodedropdown_NONE():
    browser.find_element_by_name('wep_type').click()
    elem = browser.find_element_by_name('wep_type')
    elem.send_keys(Keys.ARROW_UP)
    elem.send_keys(Keys.ARROW_UP)
    elem.send_keys(Keys.ARROW_UP)
    elem.send_keys(Keys.ENTER)
    return;

#Change Security Mode to WEP
def securitymodedropdown_WEP():
    browser.find_element_by_name('wep_type').click()
    elem = browser.find_element_by_name('wep_type')
    elem.send_keys(Keys.ARROW_UP)
    elem.send_keys(Keys.ARROW_UP)
    elem.send_keys(Keys.ARROW_UP)
    elem.send_keys(Keys.ARROW_DOWN)
    elem.send_keys(Keys.ENTER)
    return;

#Change WPA Mode to WPA2
def WPAmodedropdown_WPA2():
    browser.find_element_by_name('wpa_mode').click()
    elem = browser.find_element_by_name('wpa_mode')
    elem.send_keys(Keys.ARROW_UP)
    elem.send_keys(Keys.ARROW_UP)
    elem.send_keys(Keys.ARROW_DOWN)
    elem.send_keys(Keys.ENTER)
    return;

#Change WPA Mode to Auto
def WPAmodedropdown_AUTO():
    browser.find_element_by_name('wpa_mode').click()
    elem = browser.find_element_by_name('wpa_mode')
    elem.send_keys(Keys.ARROW_UP)
    elem.send_keys(Keys.ARROW_UP)
    elem.send_keys(Keys.ENTER)
    return;

#Change WPA Mode to WPA
def WPAmodedropdown_WPA():
    browser.find_element_by_name('wpa_mode').click()
    elem = browser.find_element_by_name('wpa_mode')
    elem.send_keys(Keys.ARROW_UP)
    elem.send_keys(Keys.ARROW_UP)
    elem.send_keys(Keys.ARROW_DOWN)
    elem.send_keys(Keys.ARROW_DOWN)
    elem.send_keys(Keys.ENTER)
    return;