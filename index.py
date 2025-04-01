from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Edge()

#driver.get("https://saucedemo.com")

title = driver.title
print(title)
driver.maximize_window()

username= "standard_user"
password= "secret_sauce"

login_url="https://saucedemo.com"
driver.get(login_url)

username_field=driver.find_element(By.ID,"user-name").send_keys(username)
password_field=driver.find_element(By.ID,"password").send_keys(password)
click_button=driver.find_element(By.ID,"login-button").click()

time.sleep(10)