import time
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime, date


browser = webdriver.Chrome()
modal_close = Alert(browser)
now = datetime.now()


def search(url):
    browser.get(url)
    browser.implicitly_wait(60)
    print("searchhhhhhhhhhhhhh")
    browser.maximize_window()
    time.sleep(2)


def login(username, password):
    try:
        user_id = browser.find_element(By.ID, "gw_user_id")
        user_id.send_keys(username)
        time.sleep(1)

        user_pw = browser.find_element(By.ID, "gw_user_pw")
        user_pw.send_keys(password)
        time.sleep(1)

        login_btn = browser.find_element(By.ID, "loginBtn")
        login_btn.click()
        browser.implicitly_wait(60)
        time.sleep(2)

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

        my_desk_btn = browser.find_element(By.XPATH, "//*[@id='MainNav']/li[6]/a")
        my_desk_btn.click()
        browser.implicitly_wait(60)

        ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").send_keys(
            "c"
        ).key_up(Keys.CONTROL).perform()

    except NoSuchElementException as error:
        print("Error: Element not found.")
        print(error)

    finally:
        time.sleep(2)
        print("successfully Login")


def github_login(github_url, github_name, github_password):
    now_date = datetime.fromordinal(datetime.today().toordinal()).strftime(
        "day: %Y 년/%m 월/%d 일"
    )
    try:
        print("social login start")
        browser.get(github_url)
        browser.maximize_window()
        browser.implicitly_wait(60)

        user_id = browser.find_element(By.ID, "login_field")
        user_id.send_keys(github_name)
        time.sleep(1)

        user_pw = browser.find_element(By.ID, "password")
        user_pw.send_keys(github_password)
        time.sleep(1)

        login_btn = browser.find_element(
            By.XPATH,
            "/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[2]/div/div/form/div/input[11]",
        )
        login_btn.click()
        browser.implicitly_wait(60)
        time.sleep(2)

        add_file_button = browser.find_element(
            By.XPATH,
            "//*[@id='repo-content-pjax-container']/div/div/div[3]/div[1]/div[2]/details",
        )
        add_file_button.click()
        time.sleep(1)

        create_new_file_button = browser.find_element(
            By.XPATH,
            "//*[@id='repo-content-pjax-container']/div/div/div[3]/div[1]/div[2]/details/div/ul/li[3]/form/button",
        )
        create_new_file_button.click()
        browser.implicitly_wait(60)
        time.sleep(1)

        title_input = browser.find_element(
            By.XPATH,
            "//*[@id='repo-content-pjax-container']/div/div/form[2]/div/div[1]/span/input",
        )
        title_input.send_keys(now_date)
        time.sleep(1)

        description = browser.find_element(By.XPATH, "//*[@id='code-editor']/div/pre")
        description.send_keys(Keys.CONTROL, "v")
        time.sleep(1)

        commit_new_file_button = browser.find_element(By.ID, "submit-file")
        commit_new_file_button.click()

        time.sleep(5)
        browser.quit()

        os.system("shutdown /h")

    except NoSuchElementException as error:
        print(error)
