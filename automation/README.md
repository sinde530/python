### Install

```
pip install selenium webdriver-manager datetime platform

// Code Formatting
pip install -U autopep8 or -U Remove
```

```test
import platform
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
from time import sleep


def login(groupware_url, username, password, browser):
    try:
        browser.get(groupware_url)
        print("times", now.time())
        sleep(3)

        user_id = browser.find_element(By.ID, "gw_user_id")
        user_id.click()
        user_id.send_keys(username)
        sleep(1)

        user_pw = browser.find_element(By.ID, "gw_user_pw")
        user_pw.click()
        user_pw.send_keys(password)
        sleep(1)

        login_btn = browser.find_element(By.ID, "loginBtn")
        login_btn.click()
        sleep(2)

    except NoSuchElementException as e:
        print("Error: Element not found.")
        print(e)

    finally:
        print("Successfully Login")


def leave_work_click(browser):
    try:
        go_to_work_btn = browser.find_element(
            By.XPATH, "//*[@id='Login_info']/p/img[1]")
        go_to_work_btn.click()
        sleep(1)

        result = browser.switch_to.alert()
        result.accept()
        print(result.text)
        sleep(100)

        mydesk_btn = browser.find_element(By.XPATH, "//*[@id='006']")
        mydesk_btn.click()
        sleep(1)

    except NoSuchElementException as e:
        print("Error: Element not found.")
        print(e)

    except UnexpectedAlertPresentException as e:
        print("Error: Unexpected alert found.")
        print(e)
        browser.switch_to.alert.accept()


if platform.system() == 'Windows':
    browser = webdriver.Chrome()
elif platform.system() == 'Darwin':
    browser = webdriver.Safari()
else:
    raise Exception("Unsupported Operating System")

groupware_url = "http://gw.meritium.co.kr"
username = "se.kim"
password = "*ksu02170331"
now = datetime.now()


login(groupware_url, username, password, browser)
leave_work_click(browser)

```
