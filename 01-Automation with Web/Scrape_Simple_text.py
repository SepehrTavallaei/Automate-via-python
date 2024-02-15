from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
def get_driver():
    # set optiokns to make Browsing easier
    options = webdriver.SafariOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable=dec=shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Safari()
    driver.get("https://automated.pythonanywhere.com")
    return driver
def main():
    driver = get_driver()
    element = driver.find_element("xpath","/html/body/div[1]/div/h1[1]")
    return element.text
print(main())
