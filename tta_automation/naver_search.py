from webdriver_setup import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = get_driver()

url = "https://www.naver.com/"
driver.get(url)

# element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "query")))
# element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="query"]')))
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '//*[@id="query"]')))
element.send_keys("python")
element.send_keys(Keys.RETURN)

time.sleep(5)
