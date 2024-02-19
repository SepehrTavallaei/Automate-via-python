from bs4 import BeautifulSoup
from selenium import webdriver
import requests

url = 'https://www.digikala.com/search/category-mobile-phone/apple/?camCode=582&camCode=582'
def get_driver():
    options = webdriver.SafariOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable=dec=shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Safari()
    driver.get("https://www.digikala.com/search/category-mobile-phone/apple/?camCode=582&camCode=582")
    return  driver

def main():
    driver = get_driver()
    price = driver.find_element('xpath','/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div/h1')
    
    print(price)

main()
# //*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div/h1
# /html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div/h1