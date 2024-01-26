import time
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

from webdriver_setup import get_driver

def login():
  load_dotenv()
  url = os.environ.get("GMK_URL")
  email = os.environ.get("EMAIL")
  password = os.environ.get("PASSWORD")


  try:
    driver = get_driver()

    driver.get(url)
    driver.implicitly_wait(10)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#typeMemberInputId')))
    element.send_keys(email)

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#typeMemberInputPassword')))
    element.send_keys(password)

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#btn_memberLogin')))
    element.send_keys(Keys.RETURN)

    time.sleep(10)
  except:
    driver.quit()

