from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime, date
from selenium import webdriver
from dotenv import load_dotenv
import time
import os

def githubLogin(github_url, github_name, github_password):
    now_date = datetime.fromordinal(datetime.today().toordinal()).strftime("day: %Y 년/%m 월/%d 일")
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
        title_input.send_keys(now_date)
        time.sleep(1)

        description = browser.find_element(
            By.XPATH, "//*[@id='code-editor']/div/pre"
        )
        description.send_keys(Keys.CONTROL, 'v')
        time.sleep(1)

        commit_new_file_button = browser.find_element(By.ID, "submit-file")
        commit_new_file_button.click()

        time.sleep(5)
        browser.quit()

        os.system("shutdown /h")

    except NoSuchElementException as error:
        print(error)


load_dotenv()
github_url = os.environ.get("GITHUB_URL")
github_name = os.environ.get("GITHUB_ID")
github_password = os.environ.get("GITHUB_PASSWORD")

browser = webdriver.Chrome()
now = datetime.now()

githubLogin(github_url, github_name, github_password)
