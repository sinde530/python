from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
from time import sleep


def login(groupware_url, username, password, browser):
    try:
        browser.get(groupware_url)
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

        go_to_work_btn = browser.find_element(
            By.XPATH, "//*[@id='Login_info']/p/img[1]"
        )
        # go_to_leave_btn = browser.find_element(By.XPATH, "//*[@id='Login_info']/p/img[2]")
        go_to_work_btn.click()
        # go_to_leave_btn.click()
        sleep(1)

    except NoSuchElementException as e:
        print("Error: Element not found.")
        print(e)

    finally:
        sleep(5)
        print("successfully Login")
        browser.quit()


groupware_url = "http://gw.meritium.co.kr"
username = "se.kim"
password = "*ksu02170331"
browser = webdriver.Chrome()
now = datetime.now()

login(groupware_url, username, password, browser)


# # domain_url = "https://www.naver.com"
# groupware_url = "http://gw.meritium.co.kr"

# # browser = webdriver.Safari()
# browser = webdriver.Chrome()

# browser.get(groupware_url)
# # sleep(2)
# # browser.find_element(By.XPATH, "//a[@data-clk='log_off.login']").click()
# sleep(1)
# browser.find_element(By.ID, "gw_user_id").click()
# browser.find_element(By.ID, "gw_user_id").send_keys("se.kim")
# sleep(1)
# browser.find_element(By.ID, "gw_user_pw").click()
# browser.find_element(By.ID, "gw_user_pw").send_keys("*ksu02170331")
# sleep(1)
# browser.find_element(By.ID, "loginBtn").click()

# sleep(5)
# browser.quit()
