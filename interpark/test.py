from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("window-size=800,600")

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
url = "https://ticket.interpark.com/Gate/TPLogin.asp"
driver.get(url)


def interpark_login():  # 인터파크 로그인
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))

    driver.find_element(By.ID, "userId").send_keys("chlwldnjs0416")
    driver.find_element(By.ID, "userPwd").send_keys("#Chl4689056")
    driver.find_element(By.ID, "btn_login").click()


def booking_number_site():  # 예약번호 입력 후, 입장
    driver.get(
        "http://poticket.interpark.com/Book/BookSession.asp?GroupCode="
        # + showcode_entry.get()
        + "23002291"
    )


def date_select():
    # Select date
    while True:
        driver.switch_to.frame(driver.find_element(By.ID, "ifrmBookStep"))
        # if int(calender_entry.get()) > 0:  # 날짜 설정
        if int(1) > 0:  # 날짜 설정
            # for i in range(int(calender_entry.get())): # 해당 월 아닐시 +1씩 증가하여 해당 월 찾기.
            for i in range(int(1)):  # +1씩 증가하여 해당 월 찾기.:) 날짜 설정과 같은 넘버로 해야함.
                driver.find_element(
                    By.XPATH, "/html/body/div/div[1]/div[1]/div/span[3]").click()
                try:
                    '''
                    회차 클릭 해야함.
                    '''
                    time.sleep(100)
                    driver.find_element(
                        # By.XPATH, '(//*[@id="CellPlayDate"])' + "[" + date_entry.get() + "]"  # 회차 설정
                        # By.XPATH, '(//*[@id="CellPlayDate"])' + "[" + 21 + "]").click()  # 회차 설정
                        By.XPATH, '(//*[@id="CellPlayDate"])' + "[" + 21 + "]").click()  # 회차 설정
                    break
                except NoSuchElementException:
                    print("NoSearch")
                    #         # link_go()
                    #         # go()

                    # # Select round
                    # # round_xpath = f"/html/body/div/div[3]/div[1]/div/span/ul/li[{round_entry.get()}]/a"
                    # round_xpath = f"/html/body/div/div[3]/div[1]/div/span/ul/li['10']/a"
                    # wait.until(EC.element_to_be_clickable((By.XPATH, round_xpath))).click()

                    # # Click next button
                    # driver.switch_to.default_content()
                    # driver.find_element(By.ID, "LargeNextBtnImage").click()


def find_random_seat():  # 좌석 무작위로 설정
    driver.switch_to.default_content()
    seat_frame = driver.find_element(By.NAME, "ifrmSeat")
    driver.switch_to.frame(seat_frame)

    # wait.until(EC.presence_of_element_located(
    # ))


interpark_login()  # 예약번호 입력 후, 입장
booking_number_site()  # 예약번호 입력 후, 입장
date_select()  # 상품 날짜 찾기.

# find_random_seat() # 좌석 무작위로 설정
