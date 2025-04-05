from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Edge()

login_url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(login_url)
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,".oxd-text.oxd-text--p.orangehrm-login-forgot-header").click()
#forgot_password.click()
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
driver.close()
time.sleep(30)