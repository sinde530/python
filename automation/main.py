from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# domain_url = "https://github.com/sinde530"
domain_url = "https://www.naver.com"
# groupware_url = "http://gw.meritium.co.kr"

browser = webdriver.Safari()
print(webdriver)
browser.get(domain_url)

# browser.find_element_By.xpath("//a[@data-clk='log_off.login']").click()
browser.find_element(By.XPATH, "//a[@data-clk='log_off.login']").click()

sleep(5)
browser.quit()
