import time
from selenium import webdriver


def search(url):
    browser = webdriver.Chrome()
    browser.get(url)
    browser.maximize_window()
    time.sleep(10)
