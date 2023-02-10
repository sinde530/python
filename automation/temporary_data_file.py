from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from dotenv import load_dotenv
import time
import os


def login(groupware_url, username, password, browser):
    try:
        print("########## start time: ", now.time())

        browser.get(groupware_url)
        browser.maximize_window()

        # 소요할 시간
        time.sleep(2)

        user_id = browser.find_element(By.ID, "gw_user_id")
        user_id.send_keys(username)
        time.sleep(1)

        user_pw = browser.find_element(By.ID, "gw_user_pw")
        user_pw.send_keys(password)
        time.sleep(1)

        login_btn = browser.find_element(By.ID, "loginBtn")
        login_btn.click()
        time.sleep(2)

        go_to_work_btn = browser.find_element(
            By.XPATH, "//*[@id='Login_info']/p/img[1]")
        go_to_work_btn.click()
        # go_to_leave_btn = browser.find_element(By.XPATH, "//*[@id='Login_info']/p/img[2]")
        # go_to_leave_btn.click()
        time.sleep(1)
        modal_close.accept()
        time.sleep(2)
        my_desk_mtn = browser.find_element(
            By.XPATH, "//*[@id='MainNav']/li[6]/a")
        my_desk_mtn.click()

        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='Content']/table[1]")))

        elements = browser.find_elements(By.XPATH, "//table[1]//td[2]")

        for i in elements:
            try:
                pTagText = i.text
                print(pTagText)
            except Exception as e:
                print(f"Error occured while trying to get attribute: {e}")

    except NoSuchElementException as error:
        print("Error: Element not found.")
        print(error)

    finally:
        time.sleep(5)
        print("successfully Login")

        # checked function start
        time.sleep(2)
        githubLogin(github_url, github_name, github_password, pTagText)

        print("########## exit time: ", now.time())
        browser.quit()
        
        os.system("shutdown /h")



def githubLogin(github_url, github_name, github_password, pTagText):
    try:
        print("social login start")
        browser.get(github_url)
        browser.maximize_window()

        user_id = browser.find_element(By.ID, "login_field")
        user_id.send_keys(github_name)
        time.sleep(1)

        user_pw = browser.find_element(By.ID, "password")
        user_pw.send_keys(github_password)
        time.sleep(1)

        login_btn = browser.find_element(
            By.XPATH, "/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[2]/div/div/form/div/input[11]"
        )
        login_btn.click()
        time.sleep(2)

        add_file_button = browser.find_element(
            By.XPATH, "//*[@id='repo-content-pjax-container']/div/div/div[3]/div[1]/div[2]/details")
        add_file_button.click()
        time.sleep(1)

        create_new_file_button = browser.find_element(
            By.XPATH, "//*[@id='repo-content-pjax-container']/div/div/div[3]/div[1]/div[2]/details/div/ul/li[3]/form/button")
        create_new_file_button.click()
        time.sleep(1)

        title_input = browser.find_element(
            By.XPATH, "//*[@id='repo-content-pjax-container']/div/div/form[2]/div/div[1]/span/input")
        # title_input.click()
        title_input.send_keys("commit")
        time.sleep(1)

        commit_new_file_button = browser.find_element(By.ID, "submit-file")
        commit_new_file_button.click()

        time.sleep(5)
        browser.quit()

    except NoSuchElementException as error:
        print(error)

    # 소셜로그인 url 입력
    # 소셜로그인 진행
    # 프로필 메시지 등록
    # 메시지 사진 보내기
    # 메시지 보내기


load_dotenv()
groupware_url = os.environ.get("GROUPWARE_URL")
username = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")
github_url = os.environ.get("GITHUB_URL")
github_name = os.environ.get("GITHUB_ID")
github_password = os.environ.get("GITHUB_PASSWORD")

browser = webdriver.Chrome()
now = datetime.now()
modal_close = Alert(browser)

login(groupware_url, username, password, browser)
# githubLogin(github_url, github_name, github_password)
