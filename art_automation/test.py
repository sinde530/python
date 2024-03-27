from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def random_sleep(minimum=2, maximum=5):
    """사람처럼 무작위 대기 시간을 생성합니다."""
    time.sleep(random.uniform(minimum, maximum))

def human_like_typing(element, text, min_delay=0.05, max_delay=0.25):
    """텍스트를 사람처럼 타이핑합니다."""
    for char in text:
        element.send_keys(char)
        random_sleep(min_delay, max_delay)

# 크롬 옵션 설정
chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument("disable-gpu") # 가속 사용 x
# chrome_options.add_argument(f"user-data-dir={profile_path}")
chrome_options.add_argument("profile-directory=Profile 1")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.59 Safari/537.36")
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_argument("--no-sandbox")  # This can sometimes help if you're running as root
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3, 4, 5]})")
driver.execute_script("Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']})")
driver.get('')

runtext = '메인페이지 > 리스트 1번 클릭'
xpath = '/html/body/div[2]/app-root/app-layout/ng-component/div[4]/div/div[2]/channel-project-list/div/projects-list/div/projects-list-item[1]'
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
driver.execute_script("arguments[0].setAttribute('target','_blank')", element)
element.click()

runtext = '메인페이지 > 유저 작품 > 유저이름 새탭 만들기'
xpath = '/html/body/div[2]/app-root/app-layout/ng-component/div[4]/div/div[2]/channel-project-list/project-view/div/div/aside/ng-scrollbar/div/div/div/div/div/div[1]/header/div[1]/div/div[1]/h3/a'
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
driver.execute_script("arguments[0].setAttribute('target','_blank')", element)
element.click()
driver.switch_to.window(driver.window_handles[1])

time.sleep(5)
runtext = '메인페이지 > 유저 작품 > 유저이름 새탭 만들기 > 매크로 클릭'
xpath = '//*[@id="challenge-stage"]/div/label/input'
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
element.click()
print('#', runtext)


time.sleep(30)