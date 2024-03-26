import time
import os

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_setup import get_driver
from dotenv import load_dotenv
# import pdb

def login():
  # try:
  # pdb.set_trace()

  load_dotenv()
  url = os.environ.get("GMK_URL")
  email = os.environ.get("EMAIL")
  password = os.environ.get("PASSWORD")

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
  # except NoSuchElementException as error:
  #   print("Error: Element not found.")
  #   print(error)
  # finally:
  #   time.sleep(2)
  #   print("successfully Login")

