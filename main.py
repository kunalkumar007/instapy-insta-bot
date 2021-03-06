from time import sleep
from selenium import webdriver
# from instapy_chromedriver import binary_path
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import os

# binary = FirefoxBinary(os.environ.get('FIREFOX_BIN'))

browser = webdriver.Firefox(
    firefox_binary=os.environ.get('FIREFOX_BIN'))
# browser = webdriver.Firefox(firefox_binary=binary)
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')
login_link = browser.find_element_by_xpath("//*[contains(text(), 'Log In')]")


username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys("<your username>")
password_input.send_keys("<your password>")
login_link.click()
sleep(2)

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()
sleep(5)
browser.close()
