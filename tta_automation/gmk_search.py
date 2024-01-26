from webdriver_setup import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = get_driver()

# url = "https://www.gmarket.co.kr/"
# driver.get(url)

# driver.implicitly_wait(10)
# driver.get("https://www.naver.com")
# naver_tab = driver.window_handles[0]

# driver.implicitly_wait(10)
# driver.execute_script("window.open('https://www.google.com');")
# google_tab = driver.window_handles[1]

# driver.implicitly_wait(10)
# driver.execute_script("window.open('https://www.gmarket.co.kr');")
# gmarket_tab = driver.window_handles[2]

# element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '//*[@id="query"]')))
# element.send_keys("python")
# element.send_keys(Keys.RETURN)

time.sleep(5)
