import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime, date
from selenium import webdriver
import time


browser = webdriver.Chrome()


def search(url):
    browser.get(url)
    browser.implicitly_wait(10)
    print("searchhhhhhhhhhhhhh")
    browser.maximize_window()
    time.sleep(2)


def login(username):
    try:
        user_id = browser.find_element(By.ID, "gw_user_id")
        user_id.send_keys(username)
        time.sleep(1)

        # user_pw = browser.find_element(By.ID, "gw_user_pw")
        # user_pw.send_keys(password)
        # time.sleep(1)

        # login_btn = browser.find_element(By.ID, "loginBtn")
        # login_btn.click()
        # time.sleep(2)

        # Start
        # go_to_work_btn = browser.find_element(
        #     By.XPATH, "//*[@id='Login_info']/p/img[1]")
        # go_to_work_btn.click()

        # End
        # go_to_leave_btn = browser.find_element(
        #     By.XPATH, "//*[@id='Login_info']/p/img[2]"
        # )
        # go_to_leave_btn.click()

        # time.sleep(1)
        # modal_close.accept()
        # time.sleep(2)

        # my_desk_mtn = browser.find_element(By.XPATH, "//*[@id='MainNav']/li[6]/a")
        # my_desk_mtn.click()

        # ctrl a + c
        # ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").send_keys(
        #     "c"
        # ).key_up(Keys.CONTROL).perform()

    except NoSuchElementException as error:
        print("Error: Element not found.")
        print(error)

    finally:
        time.sleep(2)
        print("successfully Login")


modal_close = Alert(browser)