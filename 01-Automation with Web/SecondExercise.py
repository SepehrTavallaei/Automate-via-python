from selenium import webdriver
import time
from datetime import datetime as dt

def get_driver():
    driver = webdriver.Safari()
    driver.get("https://automated.pythonanywhere.com")
    return driver

def clean_text(text):
    return text.split(": ")[1]

def write_file(text):
    """write input text into a text file"""
    filename = f'{dt.now().strftime("%Y-%m-%d.%H-%M-%S")}.txt'
    with open(filename,'w') as file:
        file.write(text)
def main():
    driver = get_driver()
    t1 = time.time()
    
    while True:
        time.sleep(2)
        element = driver.find_element("xpath","/html/body/div[1]/div/h1[2]")
        write_file(clean_text(element.text))
        t2 = time.time()
        if t2 - t1 >15:
            break


main()
