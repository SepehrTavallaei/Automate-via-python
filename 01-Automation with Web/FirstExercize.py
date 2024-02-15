import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

def get_driver():
    options = webdriver.SafariOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable=dec=shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Safari()
    driver.get("https://automated.pythonanywhere.com/login/")
    return  driver
def print_helper(text):
    return text.split(": ")[1]
def main():
    driver = get_driver()
    driver.find_element(by="xpath",value="/html/body/div[1]/div/div/div[3]/form/p[4]/input").send_keys("automated")
    time.sleep(2)
    driver.find_element(by="id",value="id_password").send_keys("automatedautomated"+Keys.RETURN)
    time.sleep(2)
    driver.find_element('xpath',"/html/body/nav/div/a").click()
    time.sleep(5)
    element = driver.find_element("xpath",'/html/body/div[1]/div/h1[2]')
    print(print_helper(element.text))

main()
