import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
target = "House of cruise and nasty"
number = "8148374084"
url = "https://web.telegram.org/z/"
# options = Options()
# options.add_argument('headless')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(url)
time.sleep(20)
login_btn = driver.find_element(By.XPATH, '//*[@id="auth-qr-form"]/div/button')
login_btn.send_keys(Keys.ENTER)
time.sleep(10)

enter_number = driver.find_element(By.XPATH, '//*[@id="sign-in-phone-number"]')
enter_number.send_keys(number)

next_btn = driver.find_element(By.XPATH, '//*[@id="auth-phone-number-form"]/div/form/button[1]')
next_btn.send_keys(Keys.RETURN)
time.sleep(19)


auth_code = driver.find_element(By.XPATH, '//*[@id="sign-in-code"]')
auth_keys = input()
auth_code.send_keys(auth_keys)
time.sleep(19)

pencil_btn = driver.find_element(By.XPATH, '//*[@id="new-menu"]/div[1]')
pencil_btn.send_keys(Keys.RETURN)

new_grp = driver.find_element(By.XPATH, '//*[@id="new-menu"]/div[3]/div[2]/span')
new_grp.send_keys(Keys.RETURN)

side_nav = driver.find_elements(By.XPATH, '//*[@id="column-left"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div')

scroll_function = driver.find_element(By.XPATH, '//*[@id="column-left"]/div/div[3]/div[2]/div/div[2]/div')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

for x in side_nav:
    tick = driver.find_element(By.CSS_SELECTOR, 'checkbox-field-input')
    tick.send_keys(Keys.RETURN)

nxt_btn = driver.find_element(By.XPATH, '//*[@id="column-left"]/div/div[2]/div[2]/button')
nxt_btn.send_keys(Keys.RETURN)

grp_name = "CRUISE BOAT KONNECT GRP"
grp_ning = driver.find_element(By.XPATH, '//*[@id="column-left"]/div/div[2]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[1]')
grp_ning.send_keys(grp_name)

print("success")
time.sleep(10)



