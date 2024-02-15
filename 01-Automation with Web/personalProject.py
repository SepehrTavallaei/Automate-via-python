from selenium import webdriver
import time

def get_driver():
    driver = webdriver.Safari()
    driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
    return driver

def main():
    driver = get_driver()
    while True:
        time.sleep(2)
        percentage = driver.find_element("xpath",'//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[2]')
        print(percentage.text)



main()