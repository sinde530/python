from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import time 


def login(groupware_url, username, password, browser):
    try:
        print("------------------------- times", now.time())

        browser.get(groupware_url)
        browser.maximize_window()

        # 소요할 시간
        time.sleep(3600)
        
        user_id = browser.find_element(By.ID, "gw_user_id")
        user_id.click()
        user_id.send_keys(username)
        time.sleep(1)

        user_pw = browser.find_element(By.ID, "gw_user_pw")
        user_pw.click()
        user_pw.send_keys(password)
        time.sleep(1)

        login_btn = browser.find_element(By.ID, "loginBtn")
        login_btn.click()
        time.sleep(2)

        go_to_leave_btn = browser.find_element(By.XPATH, "//*[@id='Login_info']/p/img[2]")
        go_to_leave_btn.click()
        time.sleep(1)
        
        modal_close.accept()
        time.sleep(2)
    except NoSuchElementException as error:
        print("Error: Element not found.")
        print(error)

    finally:
        time.sleep(5)
        print("successfully Login")

groupware_url = "http://gw.meritium.co.kr"
username = "se.kim"
password = "*ksu02170331"
github_url = "https://github.com/login"
github_name = "sinde530"
github_password = "*ksu02170331"

browser = webdriver.Chrome()
now = datetime.now()
modal_close = Alert(browser)

login(groupware_url, username, password, browser)
