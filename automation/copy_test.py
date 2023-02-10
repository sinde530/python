from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Chrome()
browser.get("https://sinde530.github.io/")
time.sleep(5)

# elements = browser.find_elements(By.XPATH, "//a[@href]")
# elements = browser.find_elements(By.XPATH, "//p[text()]")
elements = browser.find_elements(By.XPATH, "//*[@id='Content']/table[1]/tbody/tr/td[2]")

for i in elements:
    try:
        pTagText = i.text
        print(pTagText)
    except Exception as e:
        print(f"Error occured while trying to get attribute: {e}")

browser.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as browser:
    browser.get("https://sinde530.github.io/")
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='Content']/table[1]")))

    elements = browser.find_elements(By.XPATH, "//table[1]//td[2]")

    for i in elements:
        try:
            pTagText = i.text
            print(pTagText)
        except Exception as e:
            print(f"Error occured while trying to get attribute: {e}")