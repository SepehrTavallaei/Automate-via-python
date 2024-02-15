from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
def get_driver():
    driver = webdriver.Safari()
    driver.get("https://titan22.com/account/login?return_url=%2Faccount")
    return driver

def main():
    driver = get_driver()
    driver.find_element("id","CustomerEmail").send_keys("sepehrtavallaeim@gmail.com")
    time.sleep(2)
    driver.find_element("id","CustomerPassword").send_keys("automatedautomated"+Keys.RETURN)
    time.sleep(2)
    driver.find_element("xpath",'/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a').click()
    time.sleep(2)
    print(driver.current_url) 

main()
