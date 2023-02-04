from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
from time import sleep


def login(groupware_url, username, password, browser):
    try:
        browser.get(groupware_url)
        browser.maximize_window()

        print("times", now.time())
        sleep(5)

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

        # go_to_work_btn = browser.find_element(By.XPATH, "//*[@id='Login_info']/p/img[1]")
        # go_to_work_btn.click()
        my_desk_mtn = browser.find_element(By.XPATH, "//*[@id='MainNav']/li[6]/a")
        my_desk_mtn.click()
        # go_to_leave_btn = browser.find_element(By.XPATH, "//*[@id='Login_info']/p/img[2]")
        # go_to_leave_btn.click()
    except NoSuchElementException as error:
        print("Error: Element not found.")
        print(error)

    finally:
        sleep(5)
        print("successfully Login")
        # browser.quit()


def githubLogin(github_url, github_name, github_password):
    try:
        print("social login start")
        browser.get(github_url)
        browser.maximize_window()

        user_id = browser.find_element(By.ID, "login_field")
        user_id.click()
        user_id.send_keys(github_name)
        sleep(1)

        user_pw = browser.find_element(By.ID, "password")
        user_pw.click()
        user_pw.send_keys(github_password)
        sleep(1)

        login_btn = browser.find_element(
            By.XPATH, "//*[@id='login']/div[4]/form/div/input[11]"
        )
        login_btn.click()
        sleep(2)

        user_profile = browser.find_element(
            By.XPATH, "/html/body/div[1]/div[1]/header/div[7]/details/summary"
        )
        user_profile.click()
        sleep(2)

        your_profile = browser.find_element(
            By.XPATH, "/html/body/div[1]/div[1]/header/div[7]/details/details-menu/a[1]"
        )
        your_profile.click()
        sleep(2)

        your_repository = browser.find_element(
            By.XPATH, "/html/body/div[1]/div[5]/main/div[1]/div/div/div[2]/div/nav/a[2]"
        )
        your_repository.click()
        sleep(2)

        your_repository_name = browser.find_element(By.LINK_TEXT, "leave_data")
        your_repository_name.click()

        sleep(5)
        browser.quit()

    except NoSuchElementException as error:
        print(error)

    # 소셜로그인 url 입력
    # 소셜로그인 진행
    # 프로필 메시지 등록
    # 메시지 사진 보내기
    # 메시지 보내기


groupware_url = "http://gw.meritium.co.kr"
username = "se.kim"
password = "*ksu02170331"
github_url = "https://github.com/login"
github_name = "sinde530"
github_password = "*ksu02170331"
browser = webdriver.Chrome()
now = datetime.now()

login(groupware_url, username, password, browser)
githubLogin(github_url, github_name, github_password)
